# Known limitations

[← Back to the README](../README.md)

- **Tile overlap at default jitter** — the per-tile position jitter (an
  internal default of `create_watermark_layer` in `cli/wmcore/visible.py`, currently
  ±0.35 of `--spacing`) is not yet exposed as its own CLI flag. Combined
  with the default `--spacing 250`, tiles that land close together can
  overlap slightly, which looks a bit busy in some regions of the image.
  It's cosmetic, not a correctness bug — if it bothers you, increase
  `--spacing` or shrink `--font-size` so tiles have more room.

- **Transparent PNGs** — `--blend multiply` / `overlay` and both hidden marks (`lsb`, `spread`) leave the
  image's alpha channel exactly as it was, so a transparent PNG stays transparent, and a colour blend does not
  show the grid on fully transparent pixels (it darkens the base, and there is no base there). The default
  `--blend alpha` is a real alpha-over: where the grid is drawn it adds its own opacity to the pixel's alpha.
  The hidden marks live in the colour values, which a PNG keeps even under alpha 0; whether an editor that throws
  away the colours of fully transparent pixels removes the marks there has not been measured for editors; for
  WebP output it has: see *Output formats* below.
- **Output formats** — the format follows the output file's extension.
  - **JPEG and BMP cannot hold transparency.** A transparent input is laid on **white** *before* stamping (the web
    page does the same for JPEG), so the visible grid is drawn on those pixels too and the hidden marks sit on the
    pixels that are saved; a note (`alpha_flattened`) says so. Half-transparent pixels are blended with the white,
    not shown solid. (Before v34 the alpha band was simply dropped: transparent areas came out as whatever colour
    was stored under them, usually black.) A fully opaque image is saved exactly as before. The background is
    white; `wmcore.save_with_metadata(..., background=(r, g, b))` takes another, but there is no CLI option for it.
  - **PNG, WebP and TIFF keep the alpha channel exactly.** WebP is written lossy (Pillow's default, quality 80):
    `--invisible-mode lsb` does not survive it (the run now warns, as it already did for JPEG), the spread mark does,
    and the colours under fully transparent pixels are replaced by the encoder, so a mark that lives only under
    alpha 0 is lost in a WebP (measured: an all-transparent image kept its spread mark 4/4 in PNG and TIFF, 0/4 in
    WebP; at alpha 128 WebP kept it 4/4).
  - **Metadata** (`--author`, `--copyright`, the ID in EXIF / a PNG text chunk) is written for PNG, and for JPEG with
    `piexif`; WebP, TIFF and BMP get none (and so no `metadata` layer in `--id` runs), silently for `--author` /
    `--copyright`. The ID still rides in the hidden mark.
  - **EXIF Orientation** is applied to WebP and TIFF inputs as for JPEG/PNG; BMP carries no EXIF. One Pillow fault is
    worked around here. *Cause:* opened **by path**, an uncompressed single-strip TIFF in one of Pillow's
    memory-mappable modes (L, P, RGBA, CMYK; also big-endian RGBA) is memory-mapped, and on that route Pillow lays the
    pixel buffer out with the displayed (swapped) size instead of the stored one when the Orientation is 5-8: the
    size comes out swapped and the pixels scrambled, and `exif_transpose` cannot repair it. RGB TIFFs, compressed,
    tiled, strip-wise and planar TIFFs and Orientation 1-4 never take that route. *Fix:* every image is opened through
    `wmcore.load_image` - a file object, which Pillow cannot map, read fully before it is closed - by the embedder
    (`_watermark_image`) and by every reader that decodes pixels (`--extract`, the hidden-mark decoders), so both sides
    see one picture; Pillow's global `TiffImagePlugin.READ_LIBTIFF` flag is not touched. Locked by
    `tests/test_output_formats.py`: pixel by pixel for L, P, CMYK, RGBA and big-endian RGBA at Orientation 1-8; the
    LSB and spread marks read back from an RGBA TIFF stored sideways, in both byte orders; and a scan that fails if any
    module under `cli/` calls `Image.open` on a path again. *Read side, measured (Pillow 13.0.0):* before the fix such a copy gave
    neither mark at Orientation 5-8 (and both at 1-4); after it, both at all eight. A copy whose pixels are stored
    upright with a tag that would turn them is read as Pillow shows a TIFF - turned - and is not helped by this.
    *Limits:* measured on Pillow 13.0.0 and 12.1.1, Python 3.12.3, Linux only; the explanation comes from reading
    Pillow's Python code (`ImageFile.load`, `TiffImagePlugin`) and from experiments, **not** from the C code of
    `map_buffer`, which has not been read (the fix does not depend on it: it avoids the route). The two readers inside
    the crop/resize search (`--resync`, `--rescale`) use the same opener but have no sideways-TIFF test of their own.
    **When Pillow is upgraded, re-run `bench/experiments/tiff_probe.py`** (and the TIFF tests) before trusting this.
- **Phone photos (EXIF Orientation)** — a photo stored sideways with an Orientation tag is rotated into the
  pixels before anything is drawn, and the output carries no Orientation tag (the tool writes only the EXIF
  fields it owns: `--author`, `--copyright`, the ID; the rest of the input's EXIF, GPS included, is not carried over).
  So the grid and the hidden marks are laid out on the picture as people see it, and the output shows the same way up in
  every viewer. The output's stored size is the displayed size (a 4000×3000 file tagged Orientation 6 comes out 3000×4000).
- **A short junk `Hidden payload` on a copy with no readable mark.** Where no ID can be read, the plain decoders can
  return a short "payload" that is not an ID, and `extract` then prints `Hidden payload: ...` (garbage) instead of the
  not-found text, so the `--rescale` hint is not shown. Two measurements (Pillow 13.0.0; synthetic images from the test suite's
  generator, **not real photos**): on 200 **never-stamped** 640×480 images the LSB layer returned junk on 123 (about 3 in 5)
  and the spread text decoder on none; on a **stamped 1280×960 PNG cropped** by a screenshot-style trim, read with `--ss-key
  --no-resync`, 38 of 560 runs (about 1 in 15), mostly from the LSB layer and sometimes from the spread layer's text decoder
  (10 and 4 of the 14 cases whose layer was recorded). A rarer cousin, **fixed**: with `--ss-key` and without `--rescale`, a junk text from the spread layer's plain decode used to count as
  an answer and stop the crop re-alignment from running (7 of 724 runs of a cropped stamp, about 1 in 100), so the ID of that cropped copy
  went unread, silently. A plain read that is not a well-formed ID now also gets the crop search, and is returned unchanged if the search
  finds no ID; after the fix 0 of 425 random runs missed, and the three recorded cases that missed before read (cost: see *Time* under
  *Crop resync*). **Not fixed, on purpose:** removing the junk means tightening what the LSB and
  spread text decoders accept, which would change how every image is read (the LSB layer alone is junk on most never-stamped
  images of the kind measured), so it is to be done separately, with measurements on real photos (see
  `bench/results/P2-NOTES.md` §6.6 for the earlier filtering of the spread decoder). In none of the measured junk cases was the
  junk taken for an ID (an ID needs its check characters).
