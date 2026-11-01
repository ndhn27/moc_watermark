# Needs: pip install tifffile imagecodecs   (not in requirements.txt; only these probes use them). Put in bench/experiments/.
"""TIFF variants x EXIF Orientation 1-8 x reader (Pillow default / READ_LIBTIFF), against pixel-exact ground truth.

For each variant we build an UPRIGHT picture U, store RAW = U transformed by the inverse of Orientation o, write it
with the Orientation tag set to o, then open it the way the watermark tool does (Image.open -> exif_transpose) and
compare with U. A correct reader gives U back for all eight values.
"""
import io
import os
import sys
import tempfile
import traceback

import numpy as np
import tifffile
from PIL import Image, ImageOps, TiffImagePlugin

W, H = 96, 64  # multiples of 16 so tiled files are legal


def upright_rgb():
    rng = np.random.default_rng(7)
    a = np.clip(rng.normal(120, 6, (H, W, 3)), 0, 255).astype(np.uint8)
    a[: H // 2, : W // 2] = (230, 40, 40)
    a[: H // 2, W // 2:] = (40, 200, 60)
    a[H // 2:, : W // 2] = (50, 60, 230)
    a[H // 2:, W // 2:] = (240, 220, 40)
    a[:6, :20] = 255
    a[-6:, -10:] = 0
    return a


def raw_from_upright(a, o):
    t = lambda x: np.swapaxes(x, 0, 1)
    return {1: a, 2: a[:, ::-1], 3: a[::-1, ::-1], 4: a[::-1], 5: t(a), 6: np.rot90(a, 1),
            7: t(a)[::-1, ::-1], 8: np.rot90(a, -1)}[o]


RGB = upright_rgb()
GRAY = (RGB.astype(int) @ np.array([299, 587, 114]) // 1000).astype(np.uint8)
ALPHA = np.tile(np.linspace(0, 255, W).astype(np.uint8), (H, 1))
ALPHA[: H // 4] = 255
RGBA = np.dstack([RGB, ALPHA])
_A2 = np.full((H, W), 255, np.uint8); _A2[:8, :8] = 0
RGBA_PM = np.dstack([np.where(_A2[..., None] == 0, 0, RGB).astype(np.uint8), _A2])   # alpha 0 only with black: premultiplied == straight
CMYK = np.dstack([255 - RGB, np.full((H, W), 20, np.uint8)])
LA = np.dstack([GRAY, ALPHA])
BILEVEL = (GRAY > 110)
PAL_IDX = (GRAY // 16).astype(np.uint8)
PALETTE = [v for i in range(256) for v in ((i * 7) % 256, (i * 13) % 256, (i * 29) % 256)]
GRAY16 = (GRAY.astype(np.uint16) * 257)
RGB16 = (RGB.astype(np.uint16) * 257)
RGBA16 = (RGBA.astype(np.uint16) * 257)
F32 = GRAY.astype(np.float32) / 255.0


# ---- writers: (path, raw, o) -> None -------------------------------------------------------------------------
def w_pil(mode, **kw):
    def go(path, raw, o):
        exif = Image.Exif()
        exif[0x0112] = o
        arr = np.ascontiguousarray(raw)
        if mode in ("1", "L", "RGB", "RGBA"):
            im = Image.fromarray(arr)              # mode inferred (the explicit-mode form is deprecated)
        else:
            im = Image.fromarray(arr, mode)
        if mode == "P":
            im.putpalette(PALETTE)
        im.save(path, exif=exif, **kw)
    return go


def w_tf(**kw):
    def go(path, raw, o):
        extratags = [(274, "H", 1, o, True)]
        tifffile.imwrite(path, np.ascontiguousarray(raw), metadata=None, extratags=extratags, **kw)
    return go


def w_tf_planar(**kw):
    def go(path, raw, o):
        data = np.ascontiguousarray(np.moveaxis(raw, -1, 0))        # (S, H, W)
        tifffile.imwrite(path, data, metadata=None, planarconfig="separate", extratags=[(274, "H", 1, o, True)], **kw)
    return go


def w_tf_multipage(path, raw, o):
    other = np.ascontiguousarray(raw[::-1])  # a DIFFERENT second page; only page 0 should ever be used
    with tifffile.TiffWriter(path) as tw:
        tw.write(np.ascontiguousarray(raw), photometric="rgb", metadata=None, extratags=[(274, "H", 1, o, True)])
        tw.write(other, photometric="rgb", metadata=None, extratags=[(274, "H", 1, o, True)])


ID = lambda u: u
HI = lambda u: (u >> 8).astype(np.uint8)   # Pillow reads 16-bit RGB(A) down to 8 bit by taking the high byte

# (name, upright array, writer, expected-array fn, lossy)
V = [
    ("L raw",                   GRAY,    w_pil("L"),                                  ID, False),
    ("L lzw",                   GRAY,    w_pil("L", compression="tiff_lzw"),          ID, False),
    ("LA raw",                  LA,      w_pil("LA"),                                 ID, False),
    ("P raw (palette)",         PAL_IDX, w_pil("P"),                                  ID, False),
    ("1-bit raw",               BILEVEL, w_pil("1"),                                  ID, False),
    ("1-bit group4",            BILEVEL, w_pil("1", compression="group4"),            ID, False),
    ("RGB raw",                 RGB,     w_pil("RGB"),                                ID, False),
    ("RGB lzw",                 RGB,     w_pil("RGB", compression="tiff_lzw"),        ID, False),
    ("RGB packbits",            RGB,     w_pil("RGB", compression="packbits"),        ID, False),
    ("RGB deflate",             RGB,     w_pil("RGB", compression="tiff_adobe_deflate"), ID, False),
    ("RGB jpeg-in-tiff",        RGB,     w_pil("RGB", compression="jpeg", quality=95), ID, True),
    ("RGBA raw",                RGBA,    w_pil("RGBA"),                               ID, False),
    ("RGBA lzw",                RGBA,    w_pil("RGBA", compression="tiff_lzw"),       ID, False),
    ("RGBA packbits",           RGBA,    w_pil("RGBA", compression="packbits"),       ID, False),
    ("RGBA deflate",            RGBA,    w_pil("RGBA", compression="tiff_adobe_deflate"), ID, False),
    ("CMYK raw",                CMYK,    w_pil("CMYK"),                               ID, False),
    ("CMYK lzw",                CMYK,    w_pil("CMYK", compression="tiff_lzw"),       ID, False),
    ("gray 16-bit raw (Pillow)", GRAY16, w_pil("I;16"),                               ID, False),
    # --- layouts and flavours Pillow itself does not write: use tifffile ---
    ("RGB raw, tiled 16x16",    RGB,     w_tf(photometric="rgb", tile=(16, 16)),      ID, False),
    ("RGBA raw, tiled 16x16",   RGBA,    w_tf(photometric="rgb", tile=(16, 16), extrasamples=(2,)), ID, False),
    ("RGBA lzw, tiled 16x16",   RGBA,    w_tf(photometric="rgb", tile=(16, 16), compression="lzw", extrasamples=(2,)), ID, False),
    ("RGBA raw, 4-row strips",  RGBA,    w_tf(photometric="rgb", rowsperstrip=4, extrasamples=(2,)), ID, False),
    ("RGBA raw, planar (separate)", RGBA, w_tf_planar(photometric="rgb", extrasamples=(2,)), ID, False),
    ("RGB raw, planar (separate)", RGB,  w_tf_planar(photometric="rgb"), ID, False),
    ("RGBA lzw, planar (separate)", RGBA, w_tf_planar(photometric="rgb", compression="lzw", extrasamples=(2,)), ID, False),
    ("L raw, 4-row strips",     GRAY,    w_tf(photometric="minisblack", rowsperstrip=4), ID, False),
    ("RGB raw, 4-row strips",   RGB,     w_tf(photometric="rgb", rowsperstrip=4), ID, False),
    ("CMYK raw, 4-row strips",  CMYK,    w_tf(photometric="separated", rowsperstrip=4), ID, False),
    ("gray 16-bit raw, tiled",  GRAY16,  w_tf(photometric="minisblack", tile=(16, 16)), ID, False),
    ("RGBA raw, big-endian (MM)", RGBA,  w_tf(photometric="rgb", byteorder=">", extrasamples=(2,)), ID, False),
    ("RGBA raw, ASSOCIATED alpha", RGBA_PM, w_tf(photometric="rgb", extrasamples=(1,)),  ID, False),
    ("RGBA deflate+predictor",  RGBA,    w_tf(photometric="rgb", compression="deflate", predictor=2, extrasamples=(2,)), ID, False),
    ("RGB 16-bit raw",          RGB16,   w_tf(photometric="rgb"),                     HI, False),
    ("RGBA 16-bit raw",         RGBA16,  w_tf(photometric="rgb", extrasamples=(2,)),  HI, False),
    ("RGB 16-bit deflate+pred", RGB16,   w_tf(photometric="rgb", compression="deflate", predictor=2), HI, False),
    ("gray float32 raw",        F32,     w_tf(photometric="minisblack"),              ID, False),
    ("RGB multipage (2 pages)", RGB,     w_tf_multipage,                              ID, False),
]


def read_like_the_tool(path, via_fileobj=False):
    """What _watermark_image does before anything else: open, header check, exif_transpose.
    via_fileobj=True opens an already-open binary file instead of a path (Pillow then cannot memory-map it)."""
    if via_fileobj:
        with open(path, "rb") as f:
            base = Image.open(f)
            size_header = base.size
            out = ImageOps.exif_transpose(base)      # exif_transpose loads the pixels while the file is open
            out.load()
            return size_header, out
    base = Image.open(path)
    size_header = base.size
    base.load()
    return size_header, ImageOps.exif_transpose(base)


def compare(got_img, expect, lossy):
    got = np.asarray(got_img)
    if got.shape != expect.shape:
        return "S", f"shape {got.shape} != {expect.shape} (mode {got_img.mode})"
    if got.dtype == bool or expect.dtype == bool:
        d = (got.astype(int) != expect.astype(int)).mean()
        return ("." if d == 0 else "X"), f"mismatch {d:.2%}"
    d = np.abs(got.astype(np.float64) - expect.astype(np.float64)).mean()
    if lossy:
        return ("." if d < 6 else "X"), f"mad {d:.2f}"
    return ("." if d == 0 else "X"), f"mad {d:.3f}"


def run(reader_libtiff, via_fileobj=False):
    TiffImagePlugin.READ_LIBTIFF = reader_libtiff
    res = {}
    with tempfile.TemporaryDirectory() as td:
        for name, up, writer, expfn, lossy in V:
            row, notes = [], []
            for o in range(1, 9):
                p = os.path.join(td, "t.tif")
                try:
                    writer(p, raw_from_upright(up, o), o)
                except Exception as e:  # writer cannot build it: skip variant everywhere
                    row = None
                    notes.append(f"WRITE-FAIL {type(e).__name__}: {e}")
                    break
                try:
                    hdr, img = read_like_the_tool(p, via_fileobj)
                    c, msg = compare(img, expfn(up), lossy)
                    row.append(c)
                    if c != "." and len(notes) < 1:
                        notes.append(f"o={o}: {msg}")
                    if o == 1:
                        notes.append(f"mode={img.mode}")
                except Exception as e:
                    row.append("E")
                    if len(notes) < 2:
                        notes.append(f"o={o}: {type(e).__name__}: {str(e)[:70]}")
            res[name] = ("".join(row) if row is not None else None, notes)
    return res


if __name__ == "__main__":
    import PIL
    from PIL import features
    print(f"Pillow {PIL.__version__}, libtiff {features.version('libtiff')}, tifffile {tifffile.__version__}")
    print("legend: '.' exact/ok   X pixels wrong   S size/shape wrong   E exception   (columns = Orientation 1..8)\n")
    a = run(False)
    b = run(True)
    c = run(False, via_fileobj=True)
    w = max(len(n) for n, *_ in V)
    print(f"{'variant'.ljust(w)} | default  | libtiff  | fileobj  | notes")
    for name, *_ in V:
        ra, na = a[name]; rb, nb = b[name]; rc, nc = c[name]
        if ra is None:
            print(f"{name.ljust(w)} | (could not write: {na[0][:90]})")
            continue
        flag = "" if ra == rb == rc else "  <--"
        print(f"{name.ljust(w)} | {ra} | {rb} | {rc} | {'; '.join(na)}{flag}")
