# Video support

[← Back to the README](../README.md)

Point the CLI at a video file (`.mp4`, `.mov`, `.m4v`, `.avi`, `.mkv`,
`.webm`) and it's detected automatically — same command, no separate flag.
The watermark grid is built once and stamped onto every frame; frame
compositing is parallelized across `--workers` processes so it makes real
use of multiple cores.

If `ffmpeg` is on your `PATH`, output is re-encoded to H.264 with the
**original audio track muxed back in**, in a single pass. Without `ffmpeg`,
it falls back to OpenCV's own writer — the video still gets watermarked,
but the output has **no audio** and uses a much less efficient codec. Get
`ffmpeg` from [ffmpeg.org](https://ffmpeg.org) (or `apt install ffmpeg` /
`brew install ffmpeg`) for real use.

`--copyright` is image-only and is ignored (with a note) for video input.
`--c2pa` (and, when combined with it, `--author` — see [C2PA (Content
Credentials)](c2pa.md#c2pa-content-credentials)) works for video too.

## Invisible mark (`--invisible --invisible-mode spread`)

`--invisible-mode lsb` never survives video re-encoding (H.264 or the
OpenCV fallback are both lossy) — asking for it on a video produces a
warning and no hidden mark, not a broken one. `--invisible-mode spread`
does work for video: the same `embed_spread_spectrum()` block-DCT mark used
for images is embedded into **every frame**, inside the same worker pool
that composites the visible grid, so it doesn't cost a separate pass.

A few things are different from the image version:

- **The default embedding strength (`--ss-alpha`) is higher for video**
  (20.0 vs. images' 12.0) — measured (`bench/results/P4-NOTES.md`) against
  real `ffmpeg`/H.264 re-encoding at CRF 23 (`libx264`'s own default
  quality, not an aggressive attack): at the image default, only ~65-70% of
  frames decoded afterward; raising it to 18-20 closed that to 100% in the
  same test.
- **The key rotates every `--jitter-refresh-seconds`** (the same cadence
  the visible grid's jitter already uses, not a separate flag) — the same
  anti-frame-averaging reasoning as the grid's own jitter, but on a fixed
  time interval, deliberately **not** tied to the grid's scene-cut-triggered
  early boundaries, so that a decoder can recompute which key a given frame
  used from nothing but that frame's position, the video's fps, and
  `--jitter-refresh-seconds` (public, unlike `--ss-key` itself) — see
  `video.py`'s module docstring for why. A frame within a few positions of
  a real scene cut may use a key one segment off from what a fixed-interval
  guess expects, and simply not decode — that's expected on an otherwise
  correctly-keyed video, not a sign something's wrong.
- **`extract_invisible.py` scans every frame of the video**, not just the
  first one, and reports the full breakdown (how many frames out of how
  many decoded this ID) rather than collapsing it to a plain found/not
  found — a still image gets one decode attempt; a video gets one *per
  frame*, so unlike a still image, a low per-frame hit rate does not mean
  the mark is gone: a real video has far more frames than the handful this
  was measured on, and only one of them has to decode.
- **A video reports its layers too**, but only two of the four can exist: the spread-spectrum mark
  (the frame scan above) and the C2PA manifest. LSB and file-format metadata come back as `skipped`, with
  the reason (neither survives re-encoding / video has no such layer). C2PA is now also read when the
  frames already gave an ID, so a disagreement between them would show.

A crop that removes columns from the left and/or right (common when a repost changes aspect ratio) used to
break the video mark completely; `extract` now re-aligns each frame it could not read the plain way
(`--resync`, on by default; the report says how many frames needed it). Measured on one synthetic 640×480
clip, 60 frames, re-encoded with x264 at CRF 23: both sides trimmed 80 px 60/60, a 9:16-style centre strip
57/60, an off-grid crop 51/60 (CRF 28 off-grid: 19/60; before this, all 0/60) —
`bench/results/CROP-NOTES.md` §6. On real footage (OpenCV's vtest.avi, 768×576, 60 frames, and the same scaled to 1920×1080, 24 frames) every crop tried read every frame at CRF 23 and 28 (§10); not measured on long video, native 1080p/4K footage, or codecs other than x264.

## Crop resync (`extract --resync`, on by default)

The spread-spectrum mark is laid out in raster order over the original's 8×8 block grid, so a copy
that was **cropped** did not decode: a left/right trim changes the row length, and a screenshot trimmed to
the picture almost never starts on a multiple of 8 pixels. `extract` now works out where the original grid was,
from the copy alone: it re-finds the block-grid offset (one 8×8 correlation filter gives all 64 offsets at
once) and tries every row-length/phase combination (112 × 112, a table lookup after folding the image once,
done with an FFT). A hit is still only a canonical, check-valid ID. It runs when the unmirrored plain decode found
nothing (with a given `--ss-key`: nothing, or only text that is not an ID - a free-text payload, or junk), is cheap (tens of ms per key), covers **mirrored** copies too (the plain mirrored decodes are not run
any more: the resync search reads at least as many, measured, and picks the key and the orientation by
confidence), and reports `(recovered after re-aligning ... looks cropped)`. With `--rescale` it also reads a copy
that was **cropped and resized** (a screenshot at another zoom, trimmed): it sweeps the scale on a central patch,
refines it, and re-aligns at the restored scale. Measured (`bench/results/CROP-NOTES.md`): left/right and off-grid
crops 0 → all read on synthetic images and on 11 real photos (JPEG down to q60 there, q30 on synthetic), down
to ~25% of the image area on real photos (~5% on large synthetic ones, and on 10 MP real photos); crop + resize 84 of 84 on
7 real photos (3 zoom levels, 4 tries), and on two real 10 MP photos at x0.75 and x0.5 (not at x0.33, where the mark itself is gone);
0 false IDs on 55 mark-free images. On real footage (OpenCV's vtest.avi, 768×576 and scaled to 1080p, x264 CRF 23-28)
every crop kind went from 0 to all frames read. `--resync-budget-seconds` (default 10) caps the search; running out
reports *inconclusive*, never a wrong ID. `--no-resync` turns it off (and brings back the old mirrored decodes).

What it does **not** do, and what it costs:
- **Crop + resize needs `--rescale`** (about 0.4 s per ledger key to sweep, plus about 1 s per key to verify on an image with no mark,
  so it is not on by default), works for an unmirrored copy with its aspect ratio kept. Ledger keys are swept in rounds of 6, newest
  first, each round verified before the next is swept, so a copy of a recent stamp is read in a few seconds whatever the ledger's
  length (a 200-key ledger: 4.8 s, 42 real-photo cases against a 60-key ledger, true key last, 8 s budget: 38 read, the 4 misses all one
  densely textured photo). A copy that cannot be read, or an old stamp on a long ledger of a hard photo, runs out of its share of the
  budget and is reported as inconclusive together with how many keys it got through (`--rescale-budget-seconds` raises it). **Below about x0.5 the mark itself does not survive**, whatever the decoder
  (checked by restoring the exact scale: x0.4 and under unreadable). Real X screenshots (a photo shown at 100/75/50% in a
  1600x1000 screen): every crop of the screenshot reads at all three scales (with `--rescale` below 100%), and the whole
  screen reads at 100% and 75%; a photo at 50% in the corner of an otherwise black screen, not cropped, does not
  (bench/results/CROP-NOTES.md §8c). A screenshot that also changed colours/gamma, has an overlay or a different aspect
  ratio has not been measured.
- **Some widths cannot survive a left/right trim**, whatever the decoder: widths that are a multiple of 56
  blocks (448, 896, 1344, 1792 px ...) must keep at least 448 or 896 px; all other widths are fine
  (`bench/results/CROP-NOTES.md` §4). Top/bottom trims are never affected. Very narrow or very small crops (under
  ~25 blocks across, or ~10% of a small photo) can still be lost on real photos.
- **A wrong key reads the real ID much more often** with it on (it retries on shifted grids): 18 → 54 of 60 trials
  in the measured sample. The ID read is still the one actually embedded, never a made-up one, but the key is
  now even less of a gate. "Not a secret" was already the documented position. With several keys in the ledger the
  report picks the key and the orientation by the strongest read, not the first (an earlier version of this labelled
  44% of its copies with the wrong mirroring when the ledger held 8 keys).
- **Time:** an image with no mark now costs about what it did before this feature (0.18 s at 640×480 and 2.1 s at
  6 megapixels with a 1-key ledger, against 0.20 s and 4.1 s before crop resync existed: the three mirrored DCT decodes are gone), a
  100-key ledger 0.3 s extra at 1280×960. Copies whose wrong keys read the ID partly cost ~30-55 ms per such key. With a given
  `--ss-key`, an intact image whose spread payload is free text (not an ID) now also gets the search, which finds nothing and
  returns the text unchanged: about +0.10 s at 0.3 MP, +0.18 s at 1.2 MP, +0.56 s at 6 MP and +1.05 s at 12 MP (medians of 5 reads,
  Pillow 13.0.0), always inside `--resync-budget-seconds`; `--no-resync` skips it.
- Free-text payloads are not recovered this way, only IDs (the same reason mirrored copies are ID-only).

## Repost round trip (`bench/repost_roundtrip.py`) — the test that has to be run on real platforms

Every robustness number in this README was measured against a local stand-in (Pillow JPEG, ffmpeg/x264, a viewer's resize); none
was measured against a platform. YouTube, Facebook, Telegram, TikTok, X and Instagram each resize, re-encode and strip metadata in
their own way, so the honest status is: **not measured on any real platform.** The script does the bookkeeping so that the run is
cheap: `prepare` stamps your own photos/videos (ID + spread-spectrum mark + ledger, as in normal use) into an `upload/` folder and a
manifest; you post them, download the posted copies back into a folder per platform, and `check` reads every downloaded file and prints
one row per file — whether an ID was read and which upload it is, what each layer (LSB / spread-spectrum / metadata / C2PA) found on its
own, whether the copy looks cropped or resized, how long it took — plus the uploads that no downloaded copy matched. Use `--rescale`
on `check` for images that a platform may have resized, and `--c2pa` / `--jpeg` on `prepare` for the extra layers / a JPEG variant.
`tests/test_repost_roundtrip.py` runs the same code against a local resize + JPEG q75 stand-in, which checks the bookkeeping only.
