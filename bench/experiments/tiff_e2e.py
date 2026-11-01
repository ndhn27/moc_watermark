# Needs: pip install tifffile imagecodecs   (not in requirements.txt; only these probes use them). Put in bench/experiments/.
import os, sys, tempfile, io, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "cli"))
import numpy as np, tifffile
from PIL import Image, ImageCms
import tiff_probe as P
import wmapp

FAINT = dict(text="@t", opacity=4, spacing=400, seed=1)
ICC = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
PM = np.dstack([(P.RGB.astype(int) * 128 // 255).astype(np.uint8), np.full((P.H, P.W), 128, np.uint8)])   # premultiplied, alpha 128

def ref_rgb(a):  # expected 8-bit RGB rendition of the upright picture
    if a.ndim == 2: a = np.dstack([a] * 3)
    return a[..., :3]

cases = []   # (name, writer(path), expected 8-bit RGB (H,W,3) or None)
def add(name, fn, ref): cases.append((name, fn, ref))

add("RGB lzw + ICC + 300 dpi", lambda p: Image.fromarray(P.RGB).save(p, compression="tiff_lzw", icc_profile=ICC, dpi=(300, 300)), P.RGB)
add("RGB 8-bit raw, no extras", lambda p: Image.fromarray(P.RGB).save(p), P.RGB)
add("RGBA lzw (straight alpha)", lambda p: Image.fromarray(P.RGBA).save(p, compression="tiff_lzw"), P.RGB)
add("RGB 16-bit (tifffile, deflate)", lambda p: tifffile.imwrite(p, P.RGB16, photometric="rgb", compression="deflate", metadata=None), P.RGB)
add("gray 16-bit (Pillow)", lambda p: Image.fromarray(P.GRAY16, "I;16").save(p), ref_rgb(P.GRAY))
add("gray 8-bit", lambda p: Image.fromarray(P.GRAY).save(p), ref_rgb(P.GRAY))
add("CMYK lzw", lambda p: Image.fromarray(P.CMYK, "CMYK").save(p, compression="tiff_lzw"), np.asarray(Image.fromarray(P.CMYK, "CMYK").convert("RGB")))
add("1-bit group4 (fax/scan)", lambda p: Image.fromarray(P.BILEVEL).save(p, compression="group4"), ref_rgb((P.BILEVEL * 255).astype(np.uint8)))
add("palette", lambda p: (lambda im: (im.putpalette(P.PALETTE), im.save(p)))(Image.fromarray(P.PAL_IDX, "P")), np.asarray(Image.fromarray(P.PAL_IDX, "P").convert("RGB")) if False else None)
add("float32 gray", lambda p: tifffile.imwrite(p, P.F32, photometric="minisblack", metadata=None), ref_rgb(P.GRAY))
add("RGBA ASSOCIATED alpha 128", lambda p: tifffile.imwrite(p, PM, photometric="rgb", extrasamples=(1,), metadata=None), P.RGB)
add("RGB multipage (2 pages)", lambda p: P.w_tf_multipage(p, P.RGB, 1), P.RGB)
add("RGBA raw, Orientation 6 (the Pillow case)", lambda p: P.w_pil("RGBA")(p, P.raw_from_upright(P.RGBA, 6), 6), P.RGB)
add("RGB raw, Orientation 6", lambda p: P.w_pil("RGB")(p, P.raw_from_upright(P.RGB, 6), 6), P.RGB)
add("L raw, Orientation 8", lambda p: P.w_pil("L")(p, P.raw_from_upright(P.GRAY, 8), 8), ref_rgb(P.GRAY))
add("RGB planar separate, lzw", lambda p: P.w_tf_planar(photometric="rgb")(p, P.RGB, 1), P.RGB)

print(f"{'case':44s} | result")
with tempfile.TemporaryDirectory() as td:
    for name, fn, ref in cases:
        src, out = os.path.join(td, "in.tif"), os.path.join(td, "out.tiff")
        if os.path.exists(out): os.remove(out)
        try:
            fn(src)
        except Exception as e:
            print(f"{name:44s} | (writer failed: {type(e).__name__}: {str(e)[:60]})"); continue
        try:
            r = wmapp.watermark(src, out, **FAINT)
        except BaseException as e:
            print(f"{name:44s} | TOOL ERROR {type(e).__name__}: {str(e)[:110]}"); continue
        try:
            im = Image.open(out)
            info = f"out mode={im.mode} size={im.size} frames={getattr(im,'n_frames',1)} icc={'yes' if im.info.get('icc_profile') else 'no'} dpi={tuple(round(float(x)) for x in im.info['dpi']) if 'dpi' in im.info else '-'}"
            got = np.asarray(im.convert("RGB")).astype(int)
            if ref is not None and ref.shape == got.shape:
                d = np.abs(got - ref.astype(int)).mean()
                info += f"  | vs expected 8-bit picture: mean|diff|={d:5.1f} {'OK' if d < 4 else '<<< WRONG'}"
            elif ref is not None:
                info += f"  | SIZE MISMATCH vs expected {ref.shape[:2][::-1]}  <<< WRONG"
            print(f"{name:44s} | {info}")
        except Exception as e:
            print(f"{name:44s} | output unreadable: {type(e).__name__}: {e}")
