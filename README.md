<h1 align="center">Mộc — Diagonal Grid Watermark</h1>

<p align="center">
  Stamp images <b>and video</b> with a tiled, jittered grid watermark — plus hidden marks, a lookup ID and C2PA
  Content Credentials — instead of one corner logo that anyone can crop out.
</p>

<p align="center">
  <a href="https://github.com/ndhn27/moc_watermark/actions/workflows/tests.yml"><img alt="tests" src="https://github.com/ndhn27/moc_watermark/actions/workflows/tests.yml/badge.svg?branch=main"></a>
  <a href="LICENSE"><img alt="License: PolyForm Noncommercial 1.0.0" src="https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-orange"></a>
  <img alt="Python 3.12 | 3.13" src="https://img.shields.io/badge/python-3.12%20%7C%203.13-3776AB?logo=python&logoColor=white">
  <img alt="Images and video" src="https://img.shields.io/badge/media-images%20%2B%20video-8A2BE2">
  <img alt="C2PA Content Credentials" src="https://img.shields.io/badge/provenance-C2PA-0A66C2">
  <img alt="Web tool: runs in your browser" src="https://img.shields.io/badge/web%20tool-runs%20in%20your%20browser-2EA44F?logo=googlechrome&logoColor=white">
</p>

<table>
  <tr>
    <td align="center"><b>Before</b></td>
    <td align="center"><b>After</b> — default settings, <code>--seed 7</code></td>
  </tr>
  <tr>
    <td><img src="docs/img/demo-before.jpg" alt="A synthetic sunset landscape, unmarked"></td>
    <td><img src="docs/img/demo-after.jpg" alt="The same landscape with a tiled diagonal @yourhandle watermark"></td>
  </tr>
</table>

<p align="center"><sub>The demo image is a synthetic landscape, not a photo.</sub></p>

## Why a grid instead of a corner logo?

A logo tucked in one corner is gone the moment someone crops it out, and
small, localized AI inpainting can erase it in one pass. A watermark tiled
diagonally across the *entire* frame is a different problem to remove:
getting rid of it cleanly means repainting almost the whole image (or every
frame of a video), which is far more work and tends to leave visible
artifacts or blur — especially over detailed areas like faces or text.

## Quick start

```bash
pip install -r requirements.txt        # video with audio also needs ffmpeg on PATH

# one image, one video, or a whole folder (images and videos can be mixed)
python3 cli/watermark.py input.jpg output.jpg --text "@yourhandle"
python3 cli/watermark.py input.mp4 output.mp4 --text "@yourhandle"
python3 cli/watermark.py in/ out/ --text "@yourhandle" --batch --seed 42

# add a hidden mark that survives JPEG recompression + a short ID recorded in a local ledger
python3 cli/watermark.py input.jpg output.jpg --text "@yourhandle" --id \
    --invisible --invisible-mode spread

# later: read the ID back from a suspect copy (no key to remember, the ledger has it)
python3 cli/extract_invisible.py suspect.jpg
```

Prefer a browser? Open [`web/index.html`](web/index.html): drag in images, tune the grid, download one or all as a
`.zip`. It runs entirely client-side, nothing is uploaded. It draws a plain grid; jitter, blend modes, hidden marks and
C2PA live in the CLI (or run `python3 cli/serve.py` to get the full pipeline inside the page). Every flag is in the
[CLI reference](docs/cli.md).

## Features

- **Tiled grid with per-tile jitter** — each tile gets its own offset, opacity and rotation (`--seed` to reproduce),
  which breaks the periodicity that makes a regular grid easy to model out. In video the pattern refreshes over time
  and at scene cuts. → [Visible grid](docs/visible-mark.md)
- **Blend modes** — `--blend multiply|overlay` mixes the mark into the pixel values so it can't be peeled off as a
  separate layer. → [Visible grid](docs/visible-mark.md)
- **Content-adaptive placement** — `--adaptive` makes the grid denser and darker over faces and detailed regions, and
  tracks them across a video. → [Visible grid](docs/visible-mark.md)
- **Hidden backup marks** — a simple `lsb` mark for lossless files, or a block-DCT `spread` mark that survives JPEG
  recompression (tested down to quality 50) and block-aligned crops; resized copies can be read back with
  `--rescale`. → [Invisible marks](docs/invisible-marks.md)
- **Watermark ID & ledger** — `--id` stamps one short ID into every layer that can carry it and records it in a local
  SQLite ledger; `extract` reports what each layer found. A lookup aid, not a proof and not extra robustness.
  → [Watermark ID & ledger](docs/id-and-ledger.md)
- **C2PA Content Credentials** — `--c2pa` signs the output (images and video) so a copy can be checked against the
  signed original. Self-signed by default. → [C2PA](docs/c2pa.md)
- **Provenance metadata** — `--author` / `--copyright` written to EXIF (JPEG, with `piexif`) or PNG text chunks.
  → [Invisible marks](docs/invisible-marks.md)
- **Video** — frames processed in parallel, audio kept when ffmpeg is installed, spread-spectrum mark supported.
  → [Video support](docs/video.md)
- **Python API** — the CLI, the web page's full-pipeline mode and Python callers share one application layer
  (`cli/wmapp/`). → [Architecture & Python API](docs/architecture.md)

## What it protects against

Mộc raises the cost of **casual** removal: cropping, painting over part of the image, screenshots, re-uploads through
platforms that recompress. That is the everyday case, and most removal in the wild is casual.

It is **not** proof against a motivated adversary who knows the scheme. Regeneration (diffusion purification),
collusion/averaging across several stamped images, white-box optimization against a detector and desynchronization
(rotation, scaling, warping) can defeat any publicly known watermarking technique, this tool's included. Metadata and
C2PA sidestep that arms race but answer a different question — "does this exact file match something signed" — so a
regenerated image simply comes out unsigned. Details and references: [Threat model](docs/threat-model.md).

## Known limitations

- **`--ss-key` is not a secret.** It is a reproducibility value like `--seed`: measured on real images, a random wrong
  key still decoded a text payload about 1 time in 4.
- **The `lsb` mark only survives lossless copies.** Recompression, resizing and screenshots erase it (and lossy WebP
  does too). Use `spread` when the file may be re-encoded.
- **`spread` needs a reasonably large image.** Very small images may not have enough 8×8 blocks to carry the payload.
- **Resized or cropped copies are only recoverable within limits.** `extract --rescale` (uniform scale, opt-in,
  slower) and the crop re-alignment search work in measured cases, not in general.
- **Metadata is format-dependent.** `--author`, `--copyright` and the ID in metadata are written for PNG and, with
  `piexif`, JPEG; WebP, TIFF and BMP get none. JPEG and BMP cannot hold transparency, so it is flattened onto white.
- **The web page draws a plain grid.** Jitter, blend modes, hidden marks, C2PA and video need the CLI (or `serve.py`).
- **Tested on Linux with Python 3.12.** 3.13 has been tried in part, 3.10 and 3.11 not by hand.

The full list, with measurements, is in [Known limitations](docs/known-limitations.md).

## Documentation

| Page | What is in it |
|---|---|
| [CLI tool](docs/cli.md) | install notes, examples, every flag |
| [Web tool](docs/web-tool.md) | the browser tool, the optional server mode, hosting on GitHub Pages |
| [Visible grid](docs/visible-mark.md) | jitter, blend modes, adaptive placement, batch mode and performance |
| [Invisible marks](docs/invisible-marks.md) | `lsb` vs `spread`, `--ss-key`, resize recovery, provenance metadata |
| [Watermark ID & ledger](docs/id-and-ledger.md) | `--id`, the SQLite ledger, per-layer `extract` |
| [C2PA (Content Credentials)](docs/c2pa.md) | signing, verifying, what it proves, the self-signed default |
| [Video support](docs/video.md) | video pipeline, invisible mark in video, crop resync, repost round trip |
| [Threat model](docs/threat-model.md) | what is and is not defended against |
| [Known limitations](docs/known-limitations.md) | transparency, output formats, EXIF orientation, junk payloads |
| [Architecture & Python API](docs/architecture.md) | layers, Python API, project structure |
| [Tests](docs/testing.md) · [Benchmarks](docs/benchmarks.md) | the pytest suite and CI; the measurement framework in `bench/` |

## Tests

```bash
pip install -r requirements-dev.txt
pytest tests/
```

The video tests need an `ffmpeg` binary on PATH. GitHub Actions runs the suite on every push and pull request. More in
[Tests](docs/testing.md); measurements of how often each mark survives are in [Benchmarks](docs/benchmarks.md).

## License

[PolyForm Noncommercial License 1.0.0](LICENSE). The source is public, but this is **not** an open-source
licence in the OSI sense: commercial use is not allowed without the author's approval.

- **Free** for any noncommercial purpose: personal use, hobby projects, study, research and experiments, and use by
  charities, schools, public research bodies, public safety/health and environmental organisations and
  government institutions (the exact wording is in [LICENSE](LICENSE)).
- **Making money with it needs approval.** Anything commercial (selling it, putting it in a paid product or
  service, ...) is not covered by that licence. Ask the author first: [ndhn27 on GitHub](https://github.com/ndhn27).
- **Forks and changes are fine** for noncommercial purposes, but credit stays with the code: whoever passes on a
  copy (changed or not) must keep the licence text and the `Required Notice: Copyright (c) 2026 ndhn27` line at the
  top of [LICENSE](LICENSE).

This is a standard licence text used as published, not a custom one. The summary above is a plain-language
reading, not legal advice; where it differs from the text of [LICENSE](LICENSE), the text wins.
