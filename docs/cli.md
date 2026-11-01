# CLI tool

[← Back to the README](../README.md)

```bash
pip install -r requirements.txt
# or: pip install pillow numpy "opencv-python-headless<5" tqdm --break-system-packages
# (OpenCV 5.x is not supported yet: --adaptive needs cv2.CascadeClassifier, which 5.0 dropped)
# (video output with audio also needs an ffmpeg binary on PATH)
```

`requirements.txt` holds version **ranges**. To get the exact environment the test suite was run in (OpenCV 4.14.0.94,
c2pa-python 0.37.10, numpy 2.5.4, Pillow 13.0.0 and everything they pull in; Python ≥ 3.12):

```bash
pip install -r requirements-lock.txt
```

`pyproject.toml` carries the project metadata and the pytest settings; its dependency list is read from
`requirements.txt`, so the ranges live in one place. `pip install -e ".[dev]"` installs the dependencies plus pytest
(the repository is run as scripts and installs no Python package).

`piexif` (in `requirements.txt`) is optional: it's only needed for
`--author`/`--copyright` metadata on **JPEG** output. If it's missing,
those flags are silently skipped with a printed note — everything else,
including PNG metadata, works without it. `c2pa-python`/`cryptography`
(also in `requirements.txt`, also optional) are only needed for `--c2pa` —
see [C2PA (Content Credentials)](c2pa.md#c2pa-content-credentials) — but unlike
`piexif`, `--c2pa` fails fast with a clear error if they're missing rather
than silently skipping the signature.

If **no TrueType font is found** (see `--font-path` below): with
Pillow >= 10.1 the tool falls back to Pillow's built-in scalable font, so
`--font-size` still works, just with a different typeface than DejaVu/Arial.
On older Pillow, the fallback is a tiny fixed-size bitmap font that ignores
`--font-size` (a warning is printed). Either way, pass `--font-path
/path/to/some.ttf` for full control (or `brew install --cask
font-dejavu-sans` / your distro's `fonts-dejavu` package to match the
Linux default look).

```bash
# single image
python3 cli/watermark.py input.jpg output.jpg --text "@yourhandle"

# single video (audio kept automatically if ffmpeg is installed)
python3 cli/watermark.py input.mp4 output.mp4 --text "@yourhandle"

# whole folder (images and videos mixed), parallel, reproducible jitter
python3 cli/watermark.py input_folder/ output_folder/ --text "@yourhandle" \
    --batch --seed 42 --workers 8

# texture-aware blend + invisible backup + provenance metadata (images)
python3 cli/watermark.py input.jpg output.png --text "@yourhandle" \
    --blend multiply --invisible --author "Jane Doe" --copyright "(c) 2026 Jane Doe"

# invisible mark that survives JPEG recompression (spread-spectrum)
python3 cli/watermark.py input.jpg output.jpg --text "@yourhandle" \
    --invisible --invisible-mode spread --ss-key 20260918

# content-adaptive placement: denser + darker over faces/main subject
python3 cli/watermark.py input.jpg output.png --text "@yourhandle" \
    --blend multiply --adaptive --adaptive-strength 0.8 --adaptive-preview mask.png

# C2PA (Content Credentials) - signs the file, images AND video; see the
# docs/c2pa.md for the self-signed-by-default caveat
python3 cli/watermark.py input.jpg output.jpg --text "@yourhandle" --c2pa
python3 cli/c2pa_verify.py output.jpg

# read back the invisible mark later (scans the whole image, not just one corner)
python3 cli/extract_invisible.py output.png
python3 cli/extract_invisible.py output.jpg --mode spread --ss-key 20260918
# image was resized after stamping (slower; searches 0.5x-2x by default)
python3 cli/extract_invisible.py resized.jpg --mode spread --ss-key 20260918 --rescale
# --max-length caps how long a payload it will consider plausible while
# scanning (default 10000 bytes); raise it only if you embedded something
# longer than that with --invisible-text

# a short ID per output, recorded in a ledger (see "Watermark ID & ledger")
python3 cli/watermark.py input.jpg output.jpg --text "@yourhandle" --id \
    --invisible --invisible-mode spread
python3 cli/extract_invisible.py suspect.jpg        # no key needed: the ledger has it
python3 cli/wm_ledger.py show K3M9-QXR2-T4
```

## Options

| Flag | Default | Description |
|---|---|---|
| `--text` | *(required)* | Watermark text, e.g. `@yourhandle` |
| `--opacity` | `90` | Base opacity, 0–255 |
| `--font-size` | `36` | Font size in px |
| `--angle` | `30` | Base rotation angle in degrees |
| `--spacing` | `250` | Spacing between watermark tiles, in px |
| `--font-path` | *(auto)* | Path to a custom `.ttf` font. Auto-detect tries DejaVu Sans Bold (Linux), Arial Bold (macOS), then Arial Bold (Windows), in that order; see `DEFAULT_FONT_PATHS` in `cli/wmcore/primitives.py` |
| `--batch` | off | Treat input/output as folders (images + video, mixed) |
| `--workers` | CPU count | Parallel workers: files-in-parallel for `--batch` images, frames-in-parallel for a video |
| `--seed` | random | Seed for per-tile jitter (reuse to reproduce the same pattern) |
| `--blend` | `alpha` | `alpha`, `multiply`, or `overlay` — how the mark mixes with the base pixels |
| `--ink` | `0.32` | Mark darkness for `multiply`/`overlay`, 0–1 |
| `--invisible` | off | Also embed a hidden backup mark; see `--invisible-mode` — video only supports `spread` |
| `--invisible-mode` | `lsb` | `lsb` (pixel LSB, fast, no key, PNG-only, images only) or `spread` (block-DCT spread-spectrum, survives JPEG/H.264 recompression + block-aligned crop, needs `--ss-key`, works for video too) |
| `--ss-key` | *(random, printed)* | Key for `--invisible-mode spread`. Reproducibility value like `--seed`, **not** a secrecy mechanism — see [Invisible marks](invisible-marks.md) |
| `--ss-alpha` | `12.0` images / `20.0` video | Embedding strength for `--invisible-mode spread`. Higher survives harder recompression/noisier images at the cost of a small but real visual imprint |
| `--invisible-text` | *(same as `--text`)* | Text for the hidden mark (ignored with `--id`, which embeds the ID) |
| `--id` | off | Stamp a short random watermark ID into every layer that can carry it and record it in the ledger; see [Watermark ID & ledger](id-and-ledger.md#watermark-id--ledger---id) |
| `--id-value` | *(random)* | Use this specific ID (10 characters incl. check characters); must not already be in the ledger; not with `--batch` |
| `--grid-id` | off | With `--id`: also print the ID in the visible grid text (works for video). Makes the grid text longer |
| `--ledger` | `$WATERMARK_TOOL_LEDGER`, else `~/.watermark-tool/ledger.sqlite3` | Ledger file for `--id` (created `0600`; it stores spread-spectrum keys) |
| `--author` | — | Author name, embedded in EXIF/PNG metadata (images only) |
| `--copyright` | — | Copyright string, embedded in EXIF/PNG metadata (images only) |
| `--adaptive` | off | Detect faces/high-detail "main subject" regions and increase density there (+ darkness for multiply/overlay) |
| `--adaptive-strength` | `0.6` | 0-1, how strongly to boost density/darkness in detected regions |
| `--adaptive-detail-weight` | `0.5` | 0-1, weight of the general detail signal relative to face detection |
| `--face-cascade` | *(bundled)* | Path to a custom Haar cascade XML for face detection |
| `--adaptive-infill-divisor` | `2.0` | How much denser the extra grid is inside detected regions (spacing ÷ this) |
| `--adaptive-preview` | — | Images, single-file only: save the detected sensitivity mask as a PNG, for tuning |
| `--adaptive-track` | on | Video only: keep the sensitivity mask tracking the subject/camera across the clip (optical flow between periodic re-detections) instead of freezing it at frame 0. `--no-adaptive-track` for the old behavior |
| `--adaptive-redetect-seconds` | `1.0` | Video only, with `--adaptive-track`: how often to re-run full detection between flow-tracked frames |
| `--scene-cut-detect` | on | Video only: force an early jitter (and, with `--adaptive-track`, mask) refresh right at a detected hard scene cut. `--no-scene-cut-detect` to disable |
| `--scene-cut-threshold` | `0.12` | Video only: 0-1 grayscale-change threshold (on a downscaled frame) above which two consecutive frames count as a cut |
| `--no-shared-memory` | off | Video only: disable the shared-memory frame transport, fall back to a slower pickle-per-frame path (useful if shared memory isn't available in your environment, e.g. some sandboxes without `/dev/shm`) |
| `--jitter-refresh-seconds` | `4.0` | Video only: regenerate the jitter pattern every N seconds of output (rebuilds the worker pool at each boundary — see the performance note in [Visible grid](visible-mark.md)). `0` disables this and uses one static pattern for the whole clip — see the per-tile-jitter section above for why that's weaker |
| `--c2pa` | off | Sign the output with a C2PA (Content Credentials) manifest — images **and** video; see [C2PA (Content Credentials)](c2pa.md#c2pa-content-credentials) |
| `--c2pa-cert` | *(auto-generated dev cert)* | PEM file with your signing certificate (+ chain) for `--c2pa`. Must be given with `--c2pa-key` |
| `--c2pa-key` | *(auto-generated dev cert)* | Private key PEM matching `--c2pa-cert` |
| `--c2pa-alg` | `es256` | Signing algorithm for `--c2pa`; only relevant with your own `--c2pa-cert`/`--c2pa-key` — the auto-generated dev cert is ES256-only |
| `--c2pa-title` | *(output filename)* | Title recorded in the C2PA manifest |
