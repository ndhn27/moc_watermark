# Needs: pip install tifffile imagecodecs   (not in requirements.txt; only these probes use them). Put in bench/experiments/.
import os, sys, tempfile, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "cli"))
import numpy as np
from PIL import Image
import tiff_probe as P
import wmapp
FAINT = dict(text="@t", opacity=4, spacing=400, seed=1)
rows = []
def tryit(name, make):
    with tempfile.TemporaryDirectory() as td:
        src, out = os.path.join(td, "in.tif"), os.path.join(td, "out.tiff")
        try:
            make(src)
        except Exception as e:
            print(f"{name:26s} | (cannot write input: {type(e).__name__})"); return
        try:
            tin = Image.open(src).info.get("compression")
            wmapp.watermark(src, out, **FAINT)
            o = Image.open(out)
            print(f"{name:26s} | input compression={tin!s:20s} -> output compression={o.info.get('compression')!s:20s} mode={o.mode} size={o.size}")
        except BaseException as e:
            print(f"{name:26s} | input compression={tin!s:20s} -> TOOL ERROR {type(e).__name__}: {str(e)[:70]}  (partial output file left behind: {os.path.exists(out)})")
for c in [None, "tiff_lzw", "packbits", "tiff_adobe_deflate", "tiff_deflate", "jpeg"]:
    kw = {} if c is None else {"compression": c}
    tryit(f"RGB {c or 'raw'}", lambda p, kw=kw: Image.fromarray(P.RGB).save(p, **kw))
for c in ["group4", "group3", "tiff_ccitt", "tiff_lzw", "packbits"]:
    tryit(f"1-bit {c}", lambda p, c=c: Image.fromarray(P.BILEVEL).save(p, compression=c))
tryit("gray 8-bit group4?", lambda p: Image.fromarray(P.GRAY).save(p, compression="group4"))
