# Invisible marks and provenance metadata

[← Back to the README](../README.md)

- **Invisible backup mark** (`--invisible`) — readable back
  with `cli/extract_invisible.py`, in one of two schemes
  (`--invisible-mode`); `spread` also works for video (see [Video
  support](video.md#video-support) for what's different there), `lsb` is images only:
  - **`lsb`** (default) — a simple LSB (least significant bit) payload
    spread across the image. Lightweight, needs no key, but does **not**
    survive recompression, resizing, or screenshots — it can confirm
    provenance on a losslessly-saved (PNG) copy even if the visible grid
    gets cropped or painted over, nothing more.
  - **`spread`** — a block-DCT spread-spectrum payload (classic
    spread-spectrum watermarking — Cox et al. 1997 — adapted to carry a
    multi-byte payload). This one **does** survive ordinary JPEG
    recompression (tested clean down to quality 50) and a block-aligned
    crop, because the payload lives in mid-frequency DCT coefficients of
    each 8x8 block instead of pixel LSBs, and decoding sums the signal
    across every surviving repeat before making a bit decision (the same
    "processing gain" that makes spread-spectrum radio work). It needs
    `--ss-key` (an arbitrary integer; one is generated and printed for
    you if you don't pass one) to read the mark back, works on JPEG
    output where `lsb` cannot, is noticeably slower, and needs a
    reasonably large image (very small images may not have enough 8×8
    blocks to carry even one copy of the payload).
    **`--ss-key` is a reproducibility value, like `--seed` — it is *not*
    a secrecy or access-control mechanism.** Unlike `--seed`, this gap is
    not theoretical: because every block spreads its bit against the same
    fixed sequence (needed so a crop doesn't invalidate it — see below)
    and decoding sums that correlation across every repeat in the image, a
    wrong key whose sequence happens to have even a modest chance overlap
    with the real one gets that overlap amplified by the same combining
    step that makes the real key so reliable. **Measured on real images, a
    uniformly random wrong key has roughly a 1-in-4 chance of still
    decoding the payload correctly.** (That figure is for text payloads;
    the ID-aware reader used for `--id` marks leaks somewhat more — see
    [Watermark ID & ledger](id-and-ledger.md#watermark-id--ledger---id); and with the crop re-alignment search on, a
    wrong key reads the ID far more often, 54 of 60 in the sample in `bench/results/CROP-NOTES.md` §5.) Never treat this
    as a way to keep a payload from being read by someone who doesn't have
    the key.
    **Resized images (`extract_invisible.py --rescale`).** The mark is
    anchored to the original image's 8×8 block grid, so a resized copy
    doesn't decode as-is. `--rescale` searches for the resize that was
    applied and undoes it before decoding: a cheap sweep over scale factors
    on a small top-left patch finds where the block correlations become
    strongly bimodal, refines that on bigger patches, and only then tries
    full-image decodes (a third, pricier sweep tier kicks in as a last
    resort on images large enough to afford it — roughly 1300px+ on the
    short side). It is opt-in because it costs a few seconds per
    image (more when nothing is found), and it has real limits:
    uniform scale only (aspect ratio kept), the top-left corner must still be
    the top-left corner (a resize combined with a crop is not searched for —
    measured directly in a pilot bench run simulating that exact repost
    pattern: resize + JPEG + an unaligned crop chained in one pass, 0/3
    recovered with `--rescale` even given the full default 20s budget and
    confirmed not budget-starved, see `bench/results/p0-new-attacks/` and
    `bench/README.md`'s Attacks section), and heavy downscaling (~0.5×,
    worse with JPEG on top) can erase the mark
    outright, in which case there is nothing to find. A search this wide
    over a noisy statistic also needs guardrails against false confidence
    and unbounded runtime, so the result carries a **confidence score**
    (`--rescale`'s output prints it; the Python API returns it on
    `RescaleMatch.confidence`) — a 0–1 heuristic index built from how
    strongly the winning scale stood out, how many payload repeats backed
    it up, and how many independently tried widths agreed, **not** a
    calibrated probability — and the search runs under a **wall-clock
    budget** (`--rescale-budget-seconds`, default 20s; the Python API's
    `max_seconds`), so a stubborn "nothing here" image can't hang
    indefinitely. Hitting the budget only ever makes the search give up
    sooner — it's reported separately (as "inconclusive", not "not found")
    and can never turn a marginal decode into an accepted one. Two measured
    details explain why it is not a short list of scale factors: the
    resample has to land within ~1-2 px of the original width (a fixed
    list like
    0.5/0.75/1.25/2.0 only hit 4 of 13 test resizes), and a decode a few px
    off can validate as a junk 1-byte payload, so a result is only accepted
    if it is printable text that decodes identically at two different widths.
    On 36 synthetic test images (1280×960 to 1920×1080, resized 0.5×-2× with
    bilinear/bicubic/Lanczos, plain or JPEG 85/75) it recovered 34, i.e.
    every one that decoding at the known original size also recovers (the
    other two had lost the mark), with no wrong payloads. Those are synthetic
    images, not a survey of real photos. **The cheap scale-sweep statistic
    that drives the search *is* corner-anchored** (only the final decode step
    scans the whole image, as the next paragraph says) — at some image
    size/content combinations that corner is a bad spot to judge from and the
    search fails even though the mark is intact; see `bench/results/P0-NOTES.md`
    §1 for a worked example (a visible-grid interaction, not specific to
    resizing itself).

  Both schemes tile the payload back-to-back across the whole image (across
  pixels for `lsb`, across 8×8 blocks for `spread`) so a repeat survives a
  crop or paint-over of part of the image, and both extractors scan for a
  surviving repeat wherever it lands rather than only trusting the
  top-left corner. `lsb`'s extractor only trusts a repeat once a second
  copy elsewhere confirms it (falling back to a single uncorroborated
  match only if that's genuinely all that's left); `spread`'s extractor
  instead *combines* every repeat it can find via the correlation math
  above before deciding, which tolerates real per-repeat noise far better
  than requiring an exact match would. Both share one structural
  limitation from tiling in raster order: a crop that changes the image's
  *width* (not just height), or one that starts off the 8-pixel grid, shifts every repeat's position
  within the flattened sequence, so the plain decoders above do not read it. **`extract` now handles that
  case separately** (`--resync`, on by default — see "Crop resync" in [Video support](video.md#crop-resync-extract---resync-on-by-default)), for watermark IDs. A pilot
  bench run also saw `spread`'s plain
  decoder occasionally return a **confident wrong string** (not just fail
  to find one) after a horizontal flip — only 1 misdecode in 8 trials, too
  small a sample to quote a rate from, but worth knowing a flip's failure
  mode isn't always a clean "nothing found" (see
  `bench/results/p0-new-attacks/report.md`). The same showed up with an ID
  payload: 28 wrong strings in 1968 synthetic trials — 24 on left crops and
  pixel-unaligned crops (outside the documented range), plus 2 on the supported
  block-aligned top crop, 1 on a flip and 1 at JPEG q30 (`bench/results/P2-NOTES.md`);
  the ID decoder below returned none of them.

  **Mirrored copies (left-right, top-bottom, or both).** A mirror reverses the
  block order and reflects every block, so the plain decoder reads noise -
  but the mark is not damaged (oracle bit error rate 0.000 on the mirrored
  copies that have an oracle; plain detection 0/240), because mirroring the
  suspect image back restores the original grid exactly. `extract` therefore
  also tries the three mirrorings (`wmcore/orient.py`) and says so: "recovered
  after flipping the image back". **A watermark ID is read this way, a
  free-text payload is not:** the ID rule (a check-valid 10-character ID) has a
  false-accept chance of about 1e-10 per orientation, while the text decoder's
  rule is far looser, and on periodic never-stamped test images it returned
  junk more often the more orientations it was run on - so mirrored text
  payloads are deliberately not searched. Measured on synthetic images and on
  7 classic test photos: IDs read on 240/240 and 35/35 mirrored copies (plain
  decoder: 0/240 and 0/35), no extra false positives (0/400 and 0/28 unmarked
  images), no wrong string on an ID payload (`bench/results/P3-NOTES.md`).
  Not covered: a copy that was mirrored *and* resized (the resize search runs
  on the image as given: 0/16 before, unchanged), 90-degree rotations and
  transposes, and the `lsb` layer. Cost: about 3-4x the plain decode's time on
  an image with no mark in it; a marked, unmirrored ID is answered by the
  first attempt.

- **Provenance metadata** (`--author`, `--copyright`, images only) —
  written into real EXIF (JPEG, via `piexif`) or PNG text chunks, so tools
  that read standard metadata see attribution even without looking at the
  pixels. Anyone can strip metadata, so treat this as a complementary
  signal, not the main defense.

## Related

- **C2PA / Content Credentials** (`--c2pa`, images **and** video) — a
  cryptographically signed manifest, a fundamentally different kind of
  signal from everything else on this list: not a pattern to survive an
  edit, but a signature that a specific edit history produced this exact
  file. See the dedicated [C2PA (Content Credentials)](c2pa.md#c2pa-content-credentials)
  page for what it actually proves, the self-signed-by-default
  caveat, and full CLI usage.

- **Watermark ID & ledger** (`--id`) — one short ID per output file, written
  into every layer that can carry it and recorded in a local SQLite ledger,
  so `extract` on a suspect copy returns the ID and what it means with no
  key to remember. Not a proof and not a robustness gain; see
  [Watermark ID & ledger](id-and-ledger.md#watermark-id--ledger---id).
