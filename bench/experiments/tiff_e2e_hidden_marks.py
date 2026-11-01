# Needs: pip install tifffile imagecodecs   (not in requirements.txt; only these probes use them). Put in bench/experiments/.
import os, sys, tempfile, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "cli"))
import numpy as np
from PIL import Image
import tiff_probe as P
import wmapp, wmcore

# a larger picture so the payload fits
rng = np.random.default_rng(3)
big = np.clip(rng.normal(128, 40, (256, 384, 3)), 0, 255).astype(np.uint8)
FAINT = dict(text="@t", opacity=4, spacing=400, seed=1)
KEY = 424242
with tempfile.TemporaryDirectory() as td:
    for label, kw in [("raw", {}), ("lzw", {"compression": "tiff_lzw"}), ("jpeg-in-tiff", {"compression": "jpeg"})]:
        src = os.path.join(td, f"in_{label}.tif"); out = os.path.join(td, f"out_{label}.tiff")
        Image.fromarray(big).save(src, **kw)
        for mode in ("lsb", "spread"):
            o2 = out.replace(".tiff", f"_{mode}.tiff")
            extra = dict(invisible=True, invisible_mode=mode, invisible_text="HELLO-MARK")
            if mode == "spread": extra["ss_key"] = KEY
            try:
                wmapp.watermark(src, o2, **FAINT, **extra)
                comp = Image.open(o2).info.get("compression")
                got = wmcore.invisible.extract_invisible(o2) if mode == "lsb" else wmcore.invisible.extract_spread_spectrum(o2, KEY)
                print(f"input {label:13s} invisible={mode:6s} -> output compression={comp:10s} mark read back: {got!r}")
            except BaseException as e:
                print(f"input {label:13s} invisible={mode:6s} -> {type(e).__name__}: {str(e)[:100]}")
