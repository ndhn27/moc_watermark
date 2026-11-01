"""Output (and input) formats beyond PNG: what becomes of transparency, the hidden marks, EXIF Orientation and
metadata when the file is JPEG, BMP, WebP or TIFF. test_alpha_orientation.py covers PNG and JPEG-with-EXIF; this
file is the rest.

1. RGBA -> JPEG / BMP. Neither can keep transparency. The pipeline used to drop the alpha band, so a transparent
   pixel showed whatever colour was stored under it (black, for most exporters) and a half-transparent one looked
   solid. Now the picture is laid on white BEFORE it is stamped (the web page does the same), so the grid and the
   hidden marks sit on the pixels that get saved. Measured at the time (a 480x360 image, 6 runs each): a spread mark
   read back from a JPEG made from a mostly transparent "sticker" 6/6 times with flatten-then-stamp and 0/6 with
   stamp-then-flatten, which is why the order matters and why test_spread_mark_survives_... exists.
2. Formats that DO keep alpha (WebP, TIFF; PNG is in the other file) must keep it exactly.
3. The hidden marks per output format: LSB needs a lossless file. Pillow saves WebP lossy by default, so LSB is
   wiped there - the pipeline now warns about that (it used to warn for JPEG only).
4. EXIF Orientation for WebP and TIFF inputs (BMP has no EXIF); every input/output extension pair works;
   formats without a metadata writer do not claim the metadata layer.
5. Opening images: an uncompressed TIFF with Orientation 5-8 opened by path is decoded wrongly by Pillow (see below), so
   the embedder and every reader open images through wmcore.load_image; the tests below lock both sides.
"""

import struct
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

import wmapp
import wmcore

FAINT = dict(text="@t", opacity=4, spacing=400, seed=1)      # sparse, faint grid: the output stays close to the input
KEY = 424242

EXTS = [".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"]
FORMAT_NAME = {".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG", ".webp": "WEBP", ".bmp": "BMP", ".tif": "TIFF",
               ".tiff": "TIFF"}
KEEPS_ALPHA = (".png", ".webp", ".tif", ".tiff")
LOSSY = (".jpg", ".jpeg", ".webp")


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def _gradient(w, h, seed=5, noise=8):
    rng = np.random.default_rng(seed)
    xx, yy = np.meshgrid(np.linspace(0, 255, w), np.linspace(0, 255, h))
    return np.clip(np.stack([xx, yy, (xx + yy) / 2], -1) + rng.normal(0, noise, (h, w, 3)), 0, 255).astype(np.uint8)


def _zones(w, h):
    """Alpha: left third 0 (fully transparent), middle third 128, right third 255."""
    a = np.zeros((h, w), np.uint8)
    a[:, w // 3: 2 * w // 3] = 128
    a[:, 2 * w // 3:] = 255
    return a


def _sticker(w, h):
    """Alpha: ~10% of the picture opaque, everything else fully transparent."""
    a = np.zeros((h, w), np.uint8)
    a[h // 3: 2 * h // 3, w // 3: w // 3 + int(w * 0.3)] = 255
    return a


def _rgba(w, h, alpha, seed=5):
    arr = np.dstack([_gradient(w, h, seed, noise=12), alpha])
    arr[alpha == 0, :3] = 0                  # black under the transparent pixels, like many exporters write it
    return arr


def _save_rgba(path, w, h, alpha):
    arr = _rgba(w, h, alpha)
    kw = dict(lossless=True) if str(path).endswith(".webp") else {}
    Image.fromarray(arr, "RGBA").save(path, **kw)
    return arr[..., 3]


def _flat(path):
    """What a viewer would show for the file at `path` on a white page (straight alpha, sRGB values)."""
    rgba = np.asarray(Image.open(path).convert("RGBA")).astype(float)
    a = rgba[..., 3:4] / 255
    return rgba[..., :3] * a + 255 * (1 - a), rgba[..., 3]


# The same picture stored as every kind of input that can carry transparency.
def _in_png_rgba(tmp_path):
    p = tmp_path / "in_rgba.png"
    _save_rgba(p, 160, 120, _zones(160, 120))
    return str(p)


def _in_png_palette(tmp_path):
    p = tmp_path / "in_pal.png"
    pal = Image.new("P", (160, 120), 1)
    pal.putpalette([0, 0, 0, 200, 60, 20, 30, 120, 220] + [0] * (256 * 3 - 9))
    pal.paste(0, (0, 0, 80, 120))                                        # left half = the transparent index
    pal.save(p, transparency=0)
    return str(p)


def _in_png_la(tmp_path):
    p = tmp_path / "in_la.png"
    grey = _gradient(160, 120)[..., 0]
    Image.fromarray(np.dstack([grey, _zones(160, 120)]), "LA").save(p)
    return str(p)


def _in_webp_rgba(tmp_path):
    p = tmp_path / "in_rgba.webp"
    _save_rgba(p, 160, 120, _zones(160, 120))
    return str(p)


def _in_tiff_rgba(tmp_path):
    p = tmp_path / "in_rgba.tiff"
    _save_rgba(p, 160, 120, _zones(160, 120))
    return str(p)


TRANSPARENT_INPUTS = {"png-rgba": _in_png_rgba, "png-palette": _in_png_palette, "png-la": _in_png_la,
                      "webp-rgba": _in_webp_rgba, "tiff-rgba": _in_tiff_rgba}


def _opaque_png(tmp_path, w=160, h=120, name="in_opaque.png"):
    p = tmp_path / name
    Image.fromarray(_gradient(w, h), "RGB").save(p)
    return str(p)


# ---------------------------------------------------------------------------
# The helpers
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("background", [(255, 255, 255), (0, 0, 0), (10, 200, 30)])
def test_flatten_alpha_is_straight_alpha_over_the_background(background):
    w, h = 256, 8
    ramp = np.tile(np.arange(256, dtype=np.uint8), (h, 1))               # every alpha value 0..255
    arr = np.dstack([np.random.default_rng(1).integers(0, 256, (h, w, 3), dtype=np.uint8), ramp])
    out = np.asarray(wmcore.flatten_alpha(Image.fromarray(arr, "RGBA"), background)).astype(float)
    a = ramp[..., None] / 255.0
    want = arr[..., :3] * a + np.array(background) * (1 - a)
    assert np.abs(out - want).max() <= 1.0                               # 8-bit rounding only
    assert np.array_equal(out[:, 0], np.tile(background, (h, 1)))        # alpha 0 is exactly the background
    assert np.array_equal(out[:, 255], arr[:, 255, :3])                  # alpha 255 is exactly the picture


def test_flatten_alpha_returns_an_opaque_image_unchanged():
    rgb = Image.fromarray(_gradient(64, 48), "RGB")
    rgba = rgb.convert("RGBA")                                           # opaque, but in an RGBA container
    for img in (rgb, rgba):
        out = wmcore.flatten_alpha(img)
        assert out.mode == "RGB" and np.array_equal(np.asarray(out), np.asarray(rgb))


def _mode_rgba():
    return Image.fromarray(_rgba(32, 24, _zones(32, 24)), "RGBA")


def _mode_la():
    return Image.fromarray(np.dstack([_gradient(32, 24)[..., 0], _zones(32, 24)]), "LA")


def _mode_pa():
    im = Image.new("PA", (32, 24), (1, 255))
    im.putpalette([0, 0, 0, 200, 60, 20] + [0] * (256 * 3 - 6))
    im.putalpha(Image.fromarray(_zones(32, 24), "L"))
    return im


def _mode_palette_with_transparent_index():
    pal = Image.new("P", (32, 24), 1)
    pal.putpalette([0, 0, 0, 200, 60, 20] + [0] * (256 * 3 - 6))
    pal.paste(0, (0, 0, 16, 24))
    pal.info["transparency"] = 0
    return pal


def _mode_l_with_transparent_value():
    im = Image.fromarray(np.where(_zones(32, 24) > 0, 90, 7).astype(np.uint8), "L")
    im.info["transparency"] = 7
    return im


def _mode_rgb_with_transparent_colour():
    arr = np.zeros((24, 32, 3), np.uint8)
    arr[:] = (200, 60, 20)
    arr[:, :16] = (1, 2, 3)
    im = Image.fromarray(arr, "RGB")
    im.info["transparency"] = (1, 2, 3)
    return im


@pytest.mark.parametrize("make", [_mode_rgba, _mode_la, _mode_pa, _mode_palette_with_transparent_index,
                                  _mode_l_with_transparent_value, _mode_rgb_with_transparent_colour],
                         ids=lambda f: f.__name__[len("_mode_"):])
def test_flatten_alpha_handles_every_way_an_image_can_be_transparent(make):
    img = make()
    assert wmcore.has_transparency(img)
    out = wmcore.flatten_alpha(img)
    assert out.mode == "RGB" and out.size == img.size
    rgba = np.asarray(img.convert("RGBA")).astype(float)                 # Pillow's own reading of the transparency
    a = rgba[..., 3:4] / 255
    want = rgba[..., :3] * a + 255 * (1 - a)
    assert np.abs(np.asarray(out).astype(float) - want).max() <= 1.0
    assert np.asarray(out)[rgba[..., 3] == 0].min() == 255               # transparent really became white


def test_has_transparency_looks_at_pixels_not_at_the_container():
    assert not wmcore.has_transparency(Image.fromarray(_gradient(16, 16), "RGB"))
    assert not wmcore.has_transparency(Image.fromarray(_rgba(16, 16, np.full((16, 16), 255, np.uint8)), "RGBA"))
    one_hole = _rgba(16, 16, np.full((16, 16), 255, np.uint8))
    one_hole[3, 5, 3] = 254
    assert wmcore.has_transparency(Image.fromarray(one_hole, "RGBA"))
    unused = Image.new("P", (8, 8), 1)                                   # has a transparent index, uses none of it
    unused.info["transparency"] = 0
    assert not wmcore.has_transparency(unused)


@pytest.mark.parametrize("path,expected", [
    ("a.jpg", True), ("a.JPG", True), ("dir/a.jpeg", True), ("a.bmp", True), ("A.BMP", True),
    ("a.png", False), ("a.webp", False), ("a.tif", False), ("a.tiff", False), ("a", False),
])
def test_drops_alpha_is_decided_by_the_extension(path, expected):
    assert wmcore.drops_alpha(path) is expected


# ---------------------------------------------------------------------------
# save_with_metadata: the safety net for callers that hand it an RGBA image
# ---------------------------------------------------------------------------

def _flat_colour_rgba(w=96, h=64, colour=(40, 80, 160)):
    arr = np.zeros((h, w, 4), np.uint8)
    arr[..., :3] = colour
    arr[..., 3] = _zones(w, h)
    arr[arr[..., 3] == 0, :3] = 0
    return Image.fromarray(arr, "RGBA")


def test_save_as_jpeg_lays_transparency_on_white(tmp_path):
    w, h = 96, 64
    out = tmp_path / "o.jpg"
    wmcore.save_with_metadata(_flat_colour_rgba(w, h), str(out))
    got = np.asarray(Image.open(out)).astype(float)
    assert got[8:-8, 4: w // 3 - 8].mean() > 252                         # alpha 0 -> white, not the stored black
    mid = 255 + (np.array([40, 80, 160]) - 255) * 128 / 255              # alpha 128 -> half way to the colour
    assert np.abs(got[8:-8, w // 3 + 8: 2 * w // 3 - 8].mean(axis=(0, 1)) - mid).max() < 4
    assert np.abs(got[8:-8, 2 * w // 3 + 8: -4].mean(axis=(0, 1)) - [40, 80, 160]).max() < 4   # alpha 255 untouched


def test_save_as_jpeg_uses_the_background_it_is_given(tmp_path):
    w, h = 96, 64
    out = tmp_path / "o.jpg"
    wmcore.save_with_metadata(_flat_colour_rgba(w, h), str(out), background=(0, 0, 0))
    got = np.asarray(Image.open(out)).astype(float)
    assert got[8:-8, 4: w // 3 - 8].mean() < 3


def test_save_as_bmp_lays_transparency_on_white_exactly(tmp_path):
    w, h = 96, 64
    out = tmp_path / "o.bmp"
    wmcore.save_with_metadata(_flat_colour_rgba(w, h), str(out))
    img = Image.open(out)
    got = np.asarray(img)
    assert img.mode == "RGB"
    assert np.all(got[:, : w // 3] == 255)                               # lossless, so exactly white
    assert np.all(got[:, 2 * w // 3:] == [40, 80, 160])


@pytest.mark.parametrize("ext", [".jpg", ".bmp"])
def test_an_opaque_rgba_image_is_saved_exactly_as_before(tmp_path, ext):
    # The fix must be invisible to every image that has no transparency.
    rgba = Image.fromarray(_gradient(96, 64), "RGB").convert("RGBA")
    new, old = tmp_path / ("new" + ext), tmp_path / ("old" + ext)
    wmcore.save_with_metadata(rgba, str(new))
    if ext == ".jpg":
        rgba.convert("RGB").save(old, quality=95)
    else:
        rgba.save(old)
    assert new.read_bytes() == old.read_bytes()


@pytest.mark.parametrize("ext", [".png", ".webp", ".tiff"])
def test_formats_that_keep_alpha_are_not_flattened(tmp_path, ext):
    img = _flat_colour_rgba()
    out = tmp_path / ("o" + ext)
    wmcore.save_with_metadata(img, str(out))
    back = Image.open(out)
    assert back.mode == "RGBA"
    assert np.array_equal(np.asarray(back)[..., 3], np.asarray(img)[..., 3])


# ---------------------------------------------------------------------------
# RGBA -> JPEG / BMP through the pipeline
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("out_ext", [".jpg", ".bmp"])
@pytest.mark.parametrize("kind", sorted(TRANSPARENT_INPUTS))
def test_a_transparent_input_comes_out_on_white(tmp_path, kind, out_ext):
    src = TRANSPARENT_INPUTS[kind](tmp_path)
    out = tmp_path / ("out" + out_ext)
    wmapp.watermark(src, str(out), **FAINT)
    img = Image.open(out)
    assert img.mode == "RGB"
    want, alpha = _flat(src)
    clear = alpha == 0
    assert clear.any() and (alpha == 255).any()                          # the input really has both
    got = np.asarray(img).astype(float)
    assert got[clear].mean() > 245                                       # transparent -> white (a faint grid only dims it)
    assert np.abs(got - want).mean() < (6 if out_ext == ".jpg" else 3)  # and the rest is what a viewer would show


@pytest.mark.parametrize("out_ext", [".jpg", ".bmp"])
def test_half_transparent_pixels_are_blended_not_shown_solid(tmp_path, out_ext):
    src = _in_png_rgba(tmp_path)
    out = tmp_path / ("out" + out_ext)
    wmapp.watermark(src, str(out), **FAINT)
    got = np.asarray(Image.open(out)).astype(float)
    arr = np.asarray(Image.open(src))
    mid = (arr[..., 3] == 128)
    solid = arr[..., :3].astype(float)
    want = solid * (128 / 255) + 255 * (1 - 128 / 255)
    assert np.abs(got[mid] - want[mid]).mean() < (6 if out_ext == ".jpg" else 3)
    assert np.abs(got[mid] - solid[mid]).mean() > 20                     # i.e. visibly NOT the old, opaque look


def test_the_flattening_note_appears_only_when_something_was_flattened(tmp_path):
    transparent, opaque = _in_png_rgba(tmp_path), _opaque_png(tmp_path)
    for ext in (".jpg", ".jpeg", ".bmp"):
        r = wmapp.watermark(transparent, str(tmp_path / ("t" + ext)), **FAINT)
        flat = [n for n in r.notes if n.code == "alpha_flattened"]
        assert len(flat) == 1 and flat[0].level == "info" and flat[0].data == {"extension": ext}
        assert "white" in flat[0].message
        assert str(tmp_path) not in flat[0].message                      # no local paths in a note a server may relay
    for ext in (".png", ".webp", ".tiff"):                               # formats that keep the transparency
        r = wmapp.watermark(transparent, str(tmp_path / ("k" + ext)), **FAINT)
        assert "alpha_flattened" not in [n.code for n in r.notes]
    for ext in (".jpg", ".bmp"):                                         # nothing to flatten
        r = wmapp.watermark(opaque, str(tmp_path / ("o" + ext)), **FAINT)
        assert "alpha_flattened" not in [n.code for n in r.notes]


@pytest.mark.parametrize("ext", [".jpg", ".bmp"])
def test_an_opaque_rgba_source_gives_the_same_file_as_an_rgb_source(tmp_path, ext):
    rgb_src = _opaque_png(tmp_path)
    rgba_src = tmp_path / "in_rgba_opaque.png"
    Image.open(rgb_src).convert("RGBA").save(rgba_src)
    a, b = tmp_path / ("a" + ext), tmp_path / ("b" + ext)
    wmapp.watermark(rgb_src, str(a), **FAINT)
    wmapp.watermark(str(rgba_src), str(b), **FAINT)
    assert a.read_bytes() == b.read_bytes()


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_spread_mark_survives_jpeg_export_of_a_mostly_transparent_image(tmp_path, seed):
    # ~90% of this picture is transparent. Stamping the RGBA picture and flattening afterwards left 0/6 readable
    # (the mark was under alpha 0); flattening first, as the pipeline does, gave 6/6.
    w, h = 480, 360
    src = tmp_path / "sticker.png"
    arr = _rgba(w, h, _sticker(w, h), seed=seed)
    Image.fromarray(arr, "RGBA").save(src)
    out = tmp_path / "out.jpg"
    wmapp.watermark(str(src), str(out), text="@me", seed=1, blend="multiply",
                    invisible=True, invisible_mode="spread", ss_key=KEY)
    assert wmapp.extract(str(out), mode="spread", ss_key=KEY).text == "@me"


def test_an_id_stamp_is_found_in_a_flattened_jpeg(tmp_path):
    w, h = 480, 360
    src = tmp_path / "sticker.png"
    Image.fromarray(_rgba(w, h, _sticker(w, h)), "RGBA").save(src)
    out, ledger = tmp_path / "out.jpg", str(tmp_path / "ledger.sqlite3")
    r = wmapp.watermark(str(src), str(out), text="@t", seed=1, blend="multiply", stamp_id=True, invisible=True,
                        invisible_mode="spread", ledger=ledger)
    e = wmapp.extract(str(out), ledger=ledger)
    assert e.found and e.wm_id == r.wm_id


# ---------------------------------------------------------------------------
# WebP and TIFF keep alpha; every extension works as input and as output
# ---------------------------------------------------------------------------

HIDDEN = [
    {},
    dict(invisible=True, invisible_mode="lsb"),
    dict(invisible=True, invisible_mode="spread"),
    dict(stamp_id=True, invisible=True, invisible_mode="spread"),
]


@pytest.mark.parametrize("hidden", HIDDEN, ids=["no-hidden-mark", "lsb", "spread", "id+spread"])
@pytest.mark.parametrize("blend", [dict(blend="multiply"), dict(blend="overlay", ink=0.5)], ids=["multiply", "overlay"])
@pytest.mark.parametrize("ext", [".webp", ".tiff"])
def test_webp_and_tiff_return_the_input_alpha_exactly(tmp_path, ext, blend, hidden):
    w, h = 320, 240
    src = tmp_path / ("in" + ext)
    alpha_in = _save_rgba(src, w, h, _zones(w, h))
    kw = dict(blend, **hidden)
    if kw.get("stamp_id"):
        kw["ledger"] = str(tmp_path / "ledger.sqlite3")
    out = tmp_path / ("out" + ext)
    wmapp.watermark(str(src), str(out), text="@t", seed=1, **kw)
    img = Image.open(out)
    assert img.mode == "RGBA"
    assert np.array_equal(np.asarray(img)[..., 3], alpha_in)             # WebP's alpha plane is lossless by default


@pytest.mark.parametrize("out_ext", EXTS)
@pytest.mark.parametrize("kind", ["png-rgba", "webp-rgba", "tiff-rgba"])
def test_transparency_is_kept_where_the_output_can_hold_it_and_flattened_where_not(tmp_path, kind, out_ext):
    src = TRANSPARENT_INPUTS[kind](tmp_path)
    out = tmp_path / ("out" + out_ext)
    wmapp.watermark(src, str(out), blend="multiply", **FAINT)
    img = Image.open(out)
    _, alpha_in = _flat(src)
    if out_ext in KEEPS_ALPHA:
        assert img.mode == "RGBA"
        assert np.array_equal(np.asarray(img)[..., 3], alpha_in)
    else:
        assert img.mode == "RGB"
        assert np.asarray(img).astype(float)[alpha_in == 0].mean() > 245


@pytest.mark.parametrize("out_ext", EXTS)
@pytest.mark.parametrize("in_ext", EXTS)
def test_every_supported_input_and_output_extension_works(tmp_path, in_ext, out_ext):
    w, h = 96, 64
    arr = _gradient(w, h)
    src = tmp_path / ("in" + in_ext)
    Image.fromarray(arr, "RGB").save(src, **(dict(quality=95) if in_ext in (".jpg", ".jpeg") else {}))
    out = tmp_path / ("out" + out_ext)
    wmapp.watermark(str(src), str(out), **FAINT)
    img = Image.open(out)
    assert img.format == FORMAT_NAME[out_ext] and img.size == (w, h)
    assert np.abs(np.asarray(img.convert("RGB")).astype(int) - arr.astype(int)).mean() < 10   # lossy twice at worst


# ---------------------------------------------------------------------------
# The hidden marks, per output format
# ---------------------------------------------------------------------------

# Whether the mark can be read back from a file in this format, as measured (a 480x360 image, WebP at Pillow's
# default quality). LSB needs every bit of every pixel to survive, so it lives only in the lossless formats.
READABLE = {
    ("png", "lsb"): True, ("tiff", "lsb"): True, ("bmp", "lsb"): True, ("webp", "lsb"): False, ("jpg", "lsb"): False,
    ("png", "spread"): True, ("tiff", "spread"): True, ("bmp", "spread"): True, ("webp", "spread"): True,
    ("jpg", "spread"): True,
}


@pytest.mark.parametrize("fmt,mode", sorted(READABLE), ids=[f"{f}-{m}" for f, m in sorted(READABLE)])
def test_which_hidden_marks_each_output_format_keeps_and_whether_the_user_is_told(tmp_path, fmt, mode):
    src = _opaque_png(tmp_path, 480, 360)
    out = tmp_path / ("out." + fmt)
    kw = dict(ss_key=KEY) if mode == "spread" else {}
    r = wmapp.watermark(src, str(out), text="@me", seed=1, blend="multiply", invisible=True, invisible_mode=mode, **kw)
    readable = wmapp.extract(str(out), mode=mode, **kw).text == "@me"
    assert readable is READABLE[(fmt, mode)]
    warnings = [n for n in r.notes if n.code == "lsb_lossy_format"]
    # The warning must be true: given exactly when the LSB mark really cannot be read back, never for spread.
    assert bool(warnings) == (mode == "lsb" and not readable)
    if warnings:
        assert warnings[0].level == "warning"
        assert {"jpg": "JPEG", "webp": "WebP"}[fmt] in warnings[0].message


@pytest.mark.parametrize("fill,ext,readable", [
    (0, ".png", True), (0, ".tiff", True), (0, ".webp", False),         # WebP wipes the colour under alpha 0
    (128, ".png", True), (128, ".tiff", True), (128, ".webp", True),    # ... but keeps it under partial alpha
], ids=lambda v: str(v))
def test_a_spread_mark_under_transparent_pixels_needs_a_format_that_keeps_their_colour(tmp_path, fill, ext, readable):
    # Measured (480x360, 4 runs each): an image that is ENTIRELY alpha 0 keeps its spread mark 4/4 in PNG and TIFF
    # and 0/4 in WebP, because libwebp (Pillow's default, lossy) replaces the colours under fully transparent
    # pixels; at alpha 128 WebP keeps it 4/4. So with a WebP output a mark under transparent areas is lost - the
    # visible parts of the picture still carry it. Two runs each here.
    w, h = 480, 360
    for seed in (0, 1):
        src = tmp_path / f"in{seed}.png"
        Image.fromarray(_rgba(w, h, np.full((h, w), fill, np.uint8), seed=seed), "RGBA").save(src)
        out = tmp_path / f"out{seed}{ext}"
        wmapp.watermark(str(src), str(out), text="@me", seed=1, blend="multiply", invisible=True,
                        invisible_mode="spread", ss_key=KEY)
        assert (wmapp.extract(str(out), mode="spread", ss_key=KEY).text == "@me") is readable


@pytest.mark.parametrize("ext", [".webp", ".tiff", ".bmp"])
def test_formats_without_a_metadata_writer_do_not_claim_the_metadata_layer(tmp_path, ext):
    src = _opaque_png(tmp_path, 480, 360)
    ledger = str(tmp_path / "ledger.sqlite3")
    out = tmp_path / ("out" + ext)
    r = wmapp.watermark(src, str(out), text="@t", seed=1, stamp_id=True, invisible=True, invisible_mode="spread",
                        ledger=ledger, author="me", copyright_text="c")   # must not crash on the PNG-only chunk kwarg
    assert "metadata" not in r.id_layers and "spread" in r.id_layers
    assert wmcore.metadata.read_wm_id_field(str(out)) is None
    e = wmapp.extract(str(out), ledger=ledger)                           # the ID still comes back, through the mark
    assert e.found and e.wm_id == r.wm_id


def test_png_and_jpeg_still_claim_the_metadata_layer(tmp_path):
    src = _opaque_png(tmp_path, 480, 360)
    for ext in (".png", ".jpg"):
        r = wmapp.watermark(src, str(tmp_path / ("out" + ext)), text="@t", seed=1, stamp_id=True, invisible=True,
                            invisible_mode="spread", ledger=str(tmp_path / "ledger.sqlite3"))
        assert "metadata" in r.id_layers


# ---------------------------------------------------------------------------
# EXIF Orientation in WebP and TIFF inputs (BMP cannot carry EXIF at all)
# ---------------------------------------------------------------------------

# For tag value o, a viewer shows RAW transformed by DISPLAY[o]; so RAW = UPRIGHT transformed by the inverse.
# Written out from the EXIF spec (the same table as test_alpha_orientation.py, which checks PNG and JPEG).
def _raw_from_upright(upright, o):
    a = np.asarray(upright)
    return {
        1: a,
        2: a[:, ::-1],
        3: a[::-1, ::-1],
        4: a[::-1, :],
        5: a.swapaxes(0, 1),
        6: np.rot90(a, 1),
        7: a.swapaxes(0, 1)[::-1, ::-1],
        8: np.rot90(a, -1),
    }[o]


def _upright_image(w=96, h=64):
    # Asymmetric on both axes and distinct in every corner, so no rotation or mirror can pass by accident.
    rng = np.random.default_rng(7)
    arr = np.clip(rng.normal(120, 6, (h, w, 3)), 0, 255).astype(np.uint8)
    arr[: h // 2, : w // 2] = (230, 40, 40)
    arr[: h // 2, w // 2:] = (40, 200, 60)
    arr[h // 2:, : w // 2] = (50, 60, 230)
    arr[h // 2:, w // 2:] = (240, 220, 40)
    arr[:6, :20] = 255
    arr[-6:, -10:] = 0
    return arr


def _save_with_orientation(arr, path, o, mode="RGB", **save_kw):
    exif = Image.Exif()
    exif[0x0112] = o
    kw = dict(lossless=True) if str(path).endswith(".webp") else {}
    Image.fromarray(np.ascontiguousarray(arr), mode).save(path, exif=exif, **kw, **save_kw)
    assert Image.open(path).getexif().get(0x0112) == o                   # the input really carries the tag


@pytest.mark.parametrize("o", range(1, 9))
@pytest.mark.parametrize("ext", [".webp", ".tiff"])
def test_orientation_is_baked_into_the_pixels_for_webp_and_tiff(tmp_path, ext, o):
    upright = _upright_image()
    src, out = tmp_path / ("in" + ext), tmp_path / ("out" + ext)
    _save_with_orientation(_raw_from_upright(upright, o), src, o)
    wmapp.watermark(str(src), str(out), **FAINT)
    img = Image.open(out)
    assert img.size == (upright.shape[1], upright.shape[0])              # the displayed size, not the stored one
    assert img.getexif().get(0x0112) in (None, 1)                        # nothing left to rotate it again
    got = np.asarray(img.convert("RGB")).astype(int)
    assert np.abs(got - upright.astype(int)).mean() < 8.0                # WebP is lossy; a wrong turn is 40+


@pytest.mark.parametrize("ext,save_kw", [(".webp", {}), (".tiff", dict(compression="tiff_lzw"))],
                         ids=["webp", "tiff-lzw"])
def test_orientation_and_transparency_together_in_webp_and_tiff(tmp_path, ext, save_kw):
    upright = _upright_image()
    alpha_up = np.zeros((64, 96), np.uint8)
    alpha_up[:, 48:] = 255
    raw = np.rot90(np.dstack([upright, alpha_up]), 1)                    # the stored form for Orientation 6
    src, out = tmp_path / ("in" + ext), tmp_path / ("out" + ext)
    _save_with_orientation(raw, src, 6, mode="RGBA", **save_kw)
    wmapp.watermark(str(src), str(out), blend="multiply", **FAINT)
    got = np.asarray(Image.open(out))
    assert got.shape == (64, 96, 4)
    assert np.array_equal(got[..., 3], alpha_up)
    seen = alpha_up > 0                                                  # lossy WebP drops the colour under alpha 0
    assert np.abs(got[..., :3][seen].astype(int) - upright[seen].astype(int)).mean() < 8.0


# Pillow (checked on 13.0.0 and 12.1.1) decodes an UNCOMPRESSED RGBA TIFF wrongly when its Orientation is 5-8 (a
# transposed or rotated tag) and the file is opened BY PATH: it memory-maps the file, and that shortcut ignores the
# tag's rotation, so the size comes out swapped and the pixels scrambled (exif_transpose cannot repair it). RGB TIFFs,
# compressed RGBA TIFFs and Orientation 1-4 are fine. _watermark_image therefore opens the input through
# wmcore.load_image (a file object, which Pillow cannot map, read fully before it is closed); these tests lock that
# in, pixel by pixel.
@pytest.mark.parametrize("o", range(1, 9))
def test_rgba_tiff_orientation_uncompressed(tmp_path, o):
    upright = _upright_image()
    raw = _raw_from_upright(np.dstack([upright, np.full(upright.shape[:2], 255, np.uint8)]), o)
    src, out = tmp_path / "in.tiff", tmp_path / "out.tiff"
    _save_with_orientation(raw, src, o, mode="RGBA")
    wmapp.watermark(str(src), str(out), **FAINT)
    img = Image.open(out)
    assert img.size == (96, 64)
    assert np.abs(np.asarray(img.convert("RGB")).astype(int) - upright.astype(int)).mean() < 3.0


@pytest.mark.parametrize("o", range(1, 9))
def test_rgba_tiff_orientation_compressed_is_fine(tmp_path, o):
    upright = _upright_image()
    raw = _raw_from_upright(np.dstack([upright, np.full(upright.shape[:2], 255, np.uint8)]), o)
    src, out = tmp_path / "in.tiff", tmp_path / "out.tiff"
    _save_with_orientation(raw, src, o, mode="RGBA", compression="tiff_lzw")
    wmapp.watermark(str(src), str(out), **FAINT)
    img = Image.open(out)
    assert img.size == (96, 64)
    assert np.abs(np.asarray(img.convert("RGB")).astype(int) - upright.astype(int)).mean() < 3.0


# The Pillow fault above is not RGBA-only. Opened by path, an uncompressed L, P (palette) or CMYK TIFF, and an
# uncompressed big-endian RGBA TIFF, are decoded wrongly with Orientation 5-8 as well (measured by
# bench/experiments/tiff_probe.py on Pillow 12.1.1; swapped size, scrambled pixels), while the same files opened
# through a file object are exact. Only the RGBA test above would notice if wmcore.load_image went back to
# Image.open(path); these four kinds are each wrong on 5-8 without the file object. Orientation 1-4 are in the
# parameters too, as the neighbours that were always right.

def _write_big_endian_rgba_tiff(path, rgba, o):
    """A minimal uncompressed, single-strip, 8-bit RGBA TIFF in big-endian ('MM') byte order, with Orientation o.
    Pillow only writes little-endian files, so it cannot make this one (the probe uses tifffile; the tests need not)."""
    h, w, _ = rgba.shape
    pixels = np.ascontiguousarray(rgba, dtype=np.uint8).tobytes()
    SHORT, LONG = 3, 4
    # (tag, type, count, value); sorted by tag as the format requires. None = an offset filled in below.
    entries = [(256, LONG, 1, w), (257, LONG, 1, h), (258, SHORT, 4, None), (259, SHORT, 1, 1), (262, SHORT, 1, 2),
               (273, LONG, 1, None), (274, SHORT, 1, o), (277, SHORT, 1, 4), (278, LONG, 1, h),
               (279, LONG, 1, len(pixels)), (338, SHORT, 1, 2)]       # 338 = ExtraSamples: 2 = unassociated alpha
    bits_at = 8 + 2 + 12 * len(entries) + 4                           # right after the IFD: four SHORTs, 8, 8, 8, 8
    data_at = bits_at + 8
    blob = b"MM\x00\x2a" + struct.pack(">I", 8) + struct.pack(">H", len(entries))
    for tag, typ, count, value in entries:
        if tag == 258:
            field = struct.pack(">I", bits_at)
        elif tag == 273:
            field = struct.pack(">I", data_at)
        elif typ == SHORT:
            field = struct.pack(">HH", value, 0)                      # a SHORT sits at the left of its 4-byte field
        else:
            field = struct.pack(">I", value)
        blob += struct.pack(">HHI", tag, typ, count) + field
    blob += struct.pack(">I", 0) + struct.pack(">4H", 8, 8, 8, 8) + pixels
    with open(path, "wb") as f:
        f.write(blob)


def _uncompressed_tiff_case(path, kind, o):
    """Write an uncompressed TIFF of the given kind whose stored form is the upright picture seen through
    Orientation o, and return the RGB picture a correct reader shows (taken from the file's own mode, so palette
    and CMYK conversions cannot make the expectation drift from what was written)."""
    up = _upright_image()
    if kind == "L":
        upright_img = Image.fromarray(up).convert("L")
        raw = np.ascontiguousarray(_raw_from_upright(np.asarray(upright_img), o))
        _save_with_orientation(raw, path, o, mode="L")
    elif kind == "P":
        upright_img = Image.fromarray(up).quantize(colors=32, dither=Image.Dither.NONE)
        raw = np.ascontiguousarray(_raw_from_upright(np.asarray(upright_img), o))
        img = Image.frombytes("P", (raw.shape[1], raw.shape[0]), raw.tobytes())
        img.putpalette(upright_img.getpalette())
        _save_pil_with_orientation(img, path, o)
    elif kind == "CMYK":
        upright_img = Image.fromarray(up).convert("CMYK")
        raw = np.ascontiguousarray(_raw_from_upright(np.asarray(upright_img), o))
        _save_pil_with_orientation(Image.frombytes("CMYK", (raw.shape[1], raw.shape[0]), raw.tobytes()), path, o)
    elif kind == "RGBA-big-endian":
        upright_img = Image.fromarray(up)
        rgba = np.dstack([up, np.full(up.shape[:2], 255, np.uint8)])
        _write_big_endian_rgba_tiff(path, _raw_from_upright(rgba, o), o)
    else:
        raise AssertionError(kind)
    with Image.open(path) as check:                                  # the premises of the test, not its subject
        assert check.getexif().get(0x0112) == o
        assert check.info.get("compression") == "raw"                # uncompressed: the kind Pillow maps by path
        assert check.mode == {"L": "L", "P": "P", "CMYK": "CMYK", "RGBA-big-endian": "RGBA"}[kind]
    return np.asarray(upright_img.convert("RGB"))


def _save_pil_with_orientation(img, path, o):
    exif = Image.Exif()
    exif[0x0112] = o
    img.save(path, exif=exif)


@pytest.mark.parametrize("o", range(1, 9))
@pytest.mark.parametrize("kind", ["L", "P", "CMYK", "RGBA-big-endian"])
def test_other_uncompressed_tiff_kinds_keep_their_orientation(tmp_path, kind, o):
    src, out = tmp_path / "in.tiff", tmp_path / "out.tiff"
    expected = _uncompressed_tiff_case(src, kind, o)
    wmapp.watermark(str(src), str(out), **FAINT)
    img = Image.open(out)
    assert img.size == (96, 64)                                      # the displayed size, not the stored one
    assert np.abs(np.asarray(img.convert("RGB")).astype(int) - expected.astype(int)).mean() < 3.0


# The same fault reaches the READ side. A marked picture stored as an uncompressed RGBA TIFF, sideways, with an
# Orientation of 5-8 that turns it upright again (so the DISPLAYED picture is the one the mark was embedded in, as in a
# camera-style file), gave neither an LSB nor a spread mark when the readers opened it by path - measured, in both byte
# orders - while Orientation 1-4, and RGB or LZW files at any Orientation, read fine. The readers now go through
# wmcore.load_image, like the embedder. (A file whose pixels are stored upright with a tag that would turn them is a
# different thing: Pillow applies the tag for TIFF, so the mark is read from the turned picture; not tested here.)
_MARK = "HELLO-MARK"


@pytest.mark.parametrize("o", range(1, 9))
@pytest.mark.parametrize("mode", ["lsb", "spread"])
@pytest.mark.parametrize("kind", ["RGBA", "RGBA-big-endian"])
def test_hidden_marks_read_back_from_a_sideways_stored_uncompressed_tiff(tmp_path, kind, mode, o):
    rng = np.random.default_rng(3)
    plain = np.clip(rng.normal(128, 40, (256, 384, 3)), 0, 255).astype(np.uint8)    # big enough for the payload
    src, marked, sideways = tmp_path / "in.png", tmp_path / "marked.tiff", tmp_path / "sideways.tiff"
    Image.fromarray(plain).save(src)
    extra = dict(invisible=True, invisible_mode=mode, invisible_text=_MARK)
    read_kw = {}
    if mode == "spread":
        extra["ss_key"] = read_kw["ss_key"] = KEY
    wmapp.watermark(str(src), str(marked), **FAINT, **extra)
    with Image.open(marked) as m:
        upright = np.asarray(m.convert("RGBA"))                                       # the picture the mark lives in
    stored = _raw_from_upright(upright, o)
    if kind == "RGBA":
        _save_with_orientation(stored, sideways, o, mode="RGBA")
    else:
        _write_big_endian_rgba_tiff(sideways, stored, o)
    with Image.open(sideways) as check:                                               # the premises, not the subject
        assert check.getexif().get(0x0112) == o
        assert check.info.get("compression") == "raw"
    assert wmapp.extract(str(sideways), mode=mode, **read_kw).text == _MARK


def test_images_are_opened_only_through_wmcore_load_image():
    """Nothing under cli/ may call Image.open on a path except wmcore/imageio.py: a reader that forgets would see a
    different picture from the embedder for the TIFFs above, and nothing else would tell."""
    cli = Path(__file__).resolve().parents[1] / "cli"
    allowed = {
        "wmcore/imageio.py",     # the one place
        "wmcore/metadata.py",    # reads only the PNG/JPEG ID field from the header; no pixels
        "serve.py",              # opens uploaded BYTES (io.BytesIO), which Pillow cannot memory-map
    }
    found = {p.relative_to(cli).as_posix() for p in cli.rglob("*.py") if "Image.open(" in p.read_text(encoding="utf-8")}
    assert "wmcore/imageio.py" in found                                               # the scan itself works
    assert not found - allowed, f"open images through wmcore.load_image, not Image.open: {sorted(found - allowed)}"


def test_a_bmp_input_is_never_rotated(tmp_path):
    arr = _upright_image(w=96, h=64)
    src, out = tmp_path / "in.bmp", tmp_path / "out.bmp"
    Image.fromarray(arr, "RGB").save(src)
    wmapp.watermark(str(src), str(out), **FAINT)
    img = Image.open(out)
    assert img.size == (96, 64)
    assert np.abs(np.asarray(img).astype(int) - arr.astype(int)).mean() < 3.0
