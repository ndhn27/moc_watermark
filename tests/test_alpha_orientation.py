"""Two P1 bugs found in an external review of v31, kept fixed here:

1. Transparency: multiply/overlay, the LSB mark and the spread-spectrum mark all worked on RGB and converted
   back with Image.convert("RGBA"), which makes every pixel opaque - a transparent PNG came out opaque.
   Now the hidden marks and the colour blends keep the input's alpha unchanged (so the grid doesn't show on
   fully transparent pixels); blend="alpha" is a real alpha-over and is not asked to keep alpha.
2. EXIF Orientation: the pipeline stamped the unrotated pixels and then wrote an output with no Orientation
   tag, so a viewer that had shown the input upright showed the output turned. Now the rotation is baked into
   the pixels first and the output carries no Orientation tag.
"""

import numpy as np
import pytest
from PIL import Image

import wmapp
import wmcore


# ---------------------------------------------------------------------------
# Transparency
# ---------------------------------------------------------------------------

def _rgba(alpha_plane, w=256, h=256, seed=3):
    rng = np.random.default_rng(seed)
    arr = np.zeros((h, w, 4), np.uint8)
    arr[..., :3] = rng.integers(40, 215, (h, w, 3))
    arr[..., 3] = alpha_plane
    return Image.fromarray(arr, "RGBA")


def _alpha_patterns(w=256, h=256):
    zones = np.zeros((h, w), np.uint8)               # left third 0, middle third 128, right third 255
    zones[:, w // 3: 2 * w // 3] = 128
    zones[:, 2 * w // 3:] = 255
    ramp = np.tile(np.linspace(0, 255, w).astype(np.uint8), (h, 1))      # every alpha value 0..255
    return {
        "all-transparent": np.zeros((h, w), np.uint8),
        "all-partial": np.full((h, w), 128, np.uint8),
        "all-opaque": np.full((h, w), 255, np.uint8),
        "zones-0-128-255": zones,
        "ramp": ramp,
    }


ALPHAS = _alpha_patterns()


def _mark_layer(size):
    # A real mark layer with plenty of opacity, so "the mark did not show" is not just "the mark was empty".
    return wmcore.create_watermark_layer(size, "@t", 36, 200, 30, 120, None, seed=1)


@pytest.mark.parametrize("pattern", sorted(ALPHAS))
@pytest.mark.parametrize("mode", ["multiply", "overlay"])
def test_colour_blends_keep_the_base_alpha_exactly(pattern, mode):
    base = _rgba(ALPHAS[pattern])
    out = wmcore.composite(base, _mark_layer(base.size), mode=mode, ink=0.32)
    assert out.mode == "RGBA"
    assert np.array_equal(np.asarray(out)[..., 3], ALPHAS[pattern])


def test_colour_blends_still_draw_the_mark_where_the_base_is_opaque():
    # The fix must not turn the blend into a no-op: on an opaque base the mark darkens pixels as before.
    base = _rgba(ALPHAS["all-opaque"])
    out = wmcore.composite(base, _mark_layer(base.size), mode="multiply", ink=0.32)
    assert np.any(np.asarray(out)[..., :3] != np.asarray(base)[..., :3])


@pytest.mark.parametrize("pattern", sorted(ALPHAS))
def test_alpha_over_never_lowers_alpha_and_keeps_opaque_pixels_opaque(pattern):
    # blend="alpha" is a genuine alpha-over (unchanged behaviour): alpha can only go up, 255 stays 255.
    base = _rgba(ALPHAS[pattern])
    out_a = np.asarray(wmcore.composite(base, _mark_layer(base.size), mode="alpha"))[..., 3]
    assert np.all(out_a >= ALPHAS[pattern])
    assert np.all(out_a[ALPHAS[pattern] == 255] == 255)


@pytest.mark.parametrize("pattern", sorted(ALPHAS))
def test_lsb_mark_keeps_alpha_exactly(pattern):
    base = _rgba(ALPHAS[pattern])
    out = wmcore.embed_invisible(base, "@t")
    assert out.mode == "RGBA"
    assert np.array_equal(np.asarray(out)[..., 3], ALPHAS[pattern])


@pytest.mark.parametrize("pattern", sorted(ALPHAS))
def test_spread_mark_keeps_alpha_exactly(pattern):
    base = _rgba(ALPHAS[pattern])
    out = wmcore.embed_spread_spectrum(base, "@t", 424242)
    assert out.mode == "RGBA"
    assert np.array_equal(np.asarray(out)[..., 3], ALPHAS[pattern])


def test_embedders_still_change_the_colour_channels():
    base = _rgba(ALPHAS["zones-0-128-255"])
    for out in (wmcore.embed_invisible(base, "@t"), wmcore.embed_spread_spectrum(base, "@t", 424242)):
        assert np.any(np.asarray(out)[..., :3] != np.asarray(base)[..., :3])


def test_embedders_keep_the_transparency_entry_of_a_palette_image():
    # A palette PNG with a transparent index has no "A" band, only info["transparency"].
    pal = Image.new("P", (256, 256), 1)
    pal.putpalette([0, 0, 0, 200, 60, 20, 30, 120, 220] + [0] * (256 * 3 - 9))
    pal.paste(0, (0, 0, 128, 256))                     # left half = index 0
    pal.info["transparency"] = 0
    expected = np.asarray(pal.convert("RGBA"))[..., 3]
    assert expected.min() == 0 and expected.max() == 255
    assert np.array_equal(np.asarray(wmcore.embed_invisible(pal, "@t"))[..., 3], expected)
    assert np.array_equal(np.asarray(wmcore.embed_spread_spectrum(pal, "@t", 424242))[..., 3], expected)


def _png(tmp_path, pattern, name="in.png", w=320, h=240):
    rng = np.random.default_rng(5)
    xx, yy = np.meshgrid(np.linspace(0, 255, w), np.linspace(0, 255, h))
    arr = np.zeros((h, w, 4), np.uint8)
    arr[..., :3] = np.clip(np.stack([xx, yy, (xx + yy) / 2], -1) + rng.normal(0, 8, (h, w, 3)), 0, 255)
    arr[..., 3] = _alpha_patterns(w, h)[pattern]
    p = tmp_path / name
    Image.fromarray(arr, "RGBA").save(p)
    return str(p), arr[..., 3]


HIDDEN = [
    dict(invisible=True, invisible_mode="lsb"),
    dict(invisible=True, invisible_mode="spread"),
    dict(stamp_id=True, invisible=True, invisible_mode="spread"),
]


def _stamp(tmp_path, src, name, **kw):
    out = tmp_path / name
    if kw.get("stamp_id"):
        kw = dict(kw, ledger=str(tmp_path / "ledger.sqlite3"))
    wmapp.watermark(src, str(out), text="@t", seed=1, **kw)
    return Image.open(out)


@pytest.mark.parametrize("hidden", [{}] + HIDDEN, ids=["no-hidden-mark", "lsb", "spread", "id+spread"])
@pytest.mark.parametrize("blend", [dict(blend="multiply"), dict(blend="overlay", ink=0.5)], ids=["multiply", "overlay"])
def test_pipeline_with_a_colour_blend_returns_the_input_alpha(tmp_path, blend, hidden):
    src, alpha_in = _png(tmp_path, "zones-0-128-255")
    out = _stamp(tmp_path, src, "out.png", **blend, **hidden)
    assert out.mode == "RGBA"
    assert np.array_equal(np.asarray(out)[..., 3], alpha_in)


@pytest.mark.parametrize("hidden", HIDDEN, ids=["lsb", "spread", "id+spread"])
def test_pipeline_hidden_marks_do_not_change_the_alpha_the_visible_grid_made(tmp_path, hidden):
    # Default blend="alpha" lays the grid over the image, which legitimately raises alpha where it is drawn.
    # What the hidden marks must not do is touch alpha on top of that: compare with the same run minus the mark.
    src, alpha_in = _png(tmp_path, "zones-0-128-255")
    grid_only = np.asarray(_stamp(tmp_path, src, "grid_only.png"))[..., 3]
    assert not np.array_equal(grid_only, np.full_like(grid_only, 255))        # the reference isn't all-opaque
    with_mark = np.asarray(_stamp(tmp_path, src, "marked.png", **hidden))[..., 3]
    assert np.array_equal(with_mark, grid_only)
    assert np.all(with_mark[alpha_in == 255] == 255)


def test_hidden_marks_still_read_back_from_a_transparent_png(tmp_path):
    # Keeping alpha must not cost the marks: they live in the RGB values, which the PNG still stores.
    src, _ = _png(tmp_path, "zones-0-128-255")
    out = tmp_path / "out.png"
    r = wmapp.watermark(src, str(out), text="@me", seed=1, blend="multiply", invisible=True, invisible_mode="spread")
    assert wmapp.extract(str(out), mode="spread", ss_key=r.ss_key).text == "@me"
    out_lsb = tmp_path / "out_lsb.png"
    wmapp.watermark(src, str(out_lsb), text="@me", seed=1, invisible=True, invisible_mode="lsb")
    assert wmapp.extract(str(out_lsb), mode="lsb").text == "@me"


# ---------------------------------------------------------------------------
# EXIF Orientation
# ---------------------------------------------------------------------------

# For tag value o, a viewer shows RAW transformed by DISPLAY[o]; so RAW = UPRIGHT transformed by the inverse
# (written out from the EXIF spec, not read back from Pillow, so the test isn't checking Pillow against itself).
#   1 normal   2 mirror horizontal   3 rotate 180   4 mirror vertical
#   5 transpose (mirror along the main diagonal)   6 rotate 90 clockwise to display   7 transverse   8 rotate 270 cw
def _raw_from_upright(upright, o):
    a = np.asarray(upright)
    return {
        1: a,
        2: a[:, ::-1],
        3: a[::-1, ::-1],
        4: a[::-1, :],
        5: a.transpose(1, 0, 2),
        6: np.rot90(a, 1),                      # displaying it needs 90 degrees clockwise = np.rot90(raw, -1)
        7: a.transpose(1, 0, 2)[::-1, ::-1],
        8: np.rot90(a, -1),
    }[o]


def _upright_image(w=96, h=64):
    # Asymmetric on both axes (and distinct in every corner) so no rotation or mirror can pass by accident.
    rng = np.random.default_rng(7)
    arr = np.clip(rng.normal(120, 6, (h, w, 3)), 0, 255).astype(np.uint8)
    arr[: h // 2, : w // 2] = (230, 40, 40)
    arr[: h // 2, w // 2:] = (40, 200, 60)
    arr[h // 2:, : w // 2] = (50, 60, 230)
    arr[h // 2:, w // 2:] = (240, 220, 40)
    arr[:6, :20] = 255
    arr[-6:, -10:] = 0
    return arr


def _with_orientation(arr, path, o, **save_kw):
    exif = Image.Exif()
    exif[0x0112] = o
    Image.fromarray(np.ascontiguousarray(arr), "RGB").save(path, exif=exif, **save_kw)
    assert Image.open(path).getexif().get(0x0112) == o     # the input really carries the tag


# Faint, sparse mark so the output stays close to the upright picture and a mean-difference check is meaningful.
FAINT = dict(text="@t", opacity=4, spacing=400, seed=1)


@pytest.mark.parametrize("o", range(1, 9))
def test_png_orientation_is_baked_into_the_pixels(tmp_path, o):
    upright = _upright_image()
    raw = _raw_from_upright(upright, o)
    src, out = str(tmp_path / "in.png"), str(tmp_path / "out.png")
    _with_orientation(raw, src, o)
    wmapp.watermark(src, out, **FAINT)
    img = Image.open(out)
    assert img.size == (upright.shape[1], upright.shape[0])          # displayed size, not the stored size
    assert img.getexif().get(0x0112) in (None, 1)                    # nothing left to rotate it again
    got = np.asarray(img.convert("RGB")).astype(int)
    assert np.abs(got - upright.astype(int)).mean() < 3.0


@pytest.mark.parametrize("extra", [{}, {"author": "me"}, {"stamp_id": True}], ids=["plain", "author", "id"])
def test_the_reviewed_jpeg_case_orientation_6_stays_upright(tmp_path, extra):
    # The case from the review: stored 100x200, Orientation=6, shown 200x100 (landscape).
    upright = _upright_image(w=200, h=100)
    raw = _raw_from_upright(upright, 6)
    assert raw.shape[:2] == (200, 100)
    src, out = str(tmp_path / "in.jpg"), str(tmp_path / "out.jpg")
    _with_orientation(raw, src, 6, quality=95)
    kw = dict(FAINT, **extra)
    if extra.get("stamp_id"):
        kw["ledger"] = str(tmp_path / "ledger.sqlite3")
    wmapp.watermark(src, out, **kw)
    img = Image.open(out)
    assert img.size == (200, 100)                                    # w x h as shown, so no viewer needs the tag
    assert img.getexif().get(0x0112) in (None, 1)
    got = np.asarray(img.convert("RGB")).astype(int)
    assert np.abs(got - upright.astype(int)).mean() < 8.0            # JPEG q95 noise, not a quarter turn


def test_an_image_without_an_orientation_tag_is_untouched(tmp_path):
    upright = _upright_image()
    src, out = str(tmp_path / "in.png"), str(tmp_path / "out.png")
    Image.fromarray(upright, "RGB").save(src)
    wmapp.watermark(src, out, **FAINT)
    img = Image.open(out)
    assert img.size == (96, 64)
    assert np.abs(np.asarray(img.convert("RGB")).astype(int) - upright.astype(int)).mean() < 3.0


def test_orientation_and_transparency_together(tmp_path):
    # A sideways RGBA PNG: the alpha plane must be rotated with the colours, then kept.
    upright = _upright_image()
    alpha_up = np.zeros((64, 96), np.uint8)
    alpha_up[:, 48:] = 255
    rgba_up = np.dstack([upright, alpha_up])
    raw = np.rot90(rgba_up, 1)                                       # the stored form for Orientation 6
    src, out = str(tmp_path / "in.png"), str(tmp_path / "out.png")
    exif = Image.Exif()
    exif[0x0112] = 6
    Image.fromarray(np.ascontiguousarray(raw), "RGBA").save(src, exif=exif)
    wmapp.watermark(src, out, blend="multiply", **FAINT)
    got = np.asarray(Image.open(out))
    assert got.shape == (64, 96, 4)
    assert np.array_equal(got[..., 3], alpha_up)
