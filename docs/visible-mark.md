# Visible grid: jitter, blend modes, adaptive placement

[← Back to the README](../README.md)

A perfectly regular grid still has weaknesses: it has a strong signature in
the frequency domain (FFT) that can be estimated and subtracted, especially
across many images stamped with the same pattern, and a flat white layer can
in principle be separated from the base image. The CLI addresses both:

- **Per-tile jitter** — every tile gets its own random position offset,
  opacity, and rotation, derived from `--seed` (reuse the same seed to
  reproduce an identical pattern; omit it for a fresh one each run). This
  breaks the grid's periodicity so it's much harder to model out.
  **Video gets this refreshed over time, too** (`--jitter-refresh-seconds`,
  default `4.0`): the jitter pattern is regenerated every N seconds of
  output instead of one static pattern for the whole clip. A single
  unchanging mark stamped over moving footage is itself a collusion/
  averaging-attack target — the base content moves frame to frame but the
  mark wouldn't, so a per-pixel median across enough frames estimates and
  subtracts it, no *separate* files required the way the collusion item in the [Threat model](threat-model.md)
  otherwise assumes. Pass `0` to opt back into one static pattern for the
  whole video (only useful for exact reproducibility with older output).
  **Performance note:** each refresh rebuilds the whole worker pool, which
  has a real, roughly fixed cost per rebuild — so a short interval adds up
  fast on a short clip (rebuild overhead is a bigger fraction of total
  runtime) and gets worse with more `--workers` (more worker processes to
  spawn each time). Measured on one machine: a 6s clip took 1.82s at the
  `4.0` default vs. 6.29s at `0.3` (~3.5x); the tool prints a note if you
  set it under 1 second. Benchmark your own setup before committing to a
  very short interval for a long/production run, and only go that short if
  your threat model genuinely calls for defending against an adversary who
  can median/average frames over a window that narrow.
  **Scene cuts refresh it early, too** (`--scene-cut-detect`, on by
  default): a hard cut to a different shot forces the jitter pattern to
  regenerate right there instead of drifting a few more frames into the new
  shot before the next timed refresh happens to land — see
  `--scene-cut-threshold` in the [options table](cli.md#options). Pass `--no-scene-cut-detect`
  to go back to a purely time-based refresh.

- **Blend modes** (`--blend multiply|overlay`) — instead of a flat
  alpha-over, the mark mixes into the base image's own pixel values
  (`--ink` controls how strongly), so it can't be cleanly separated as its
  own layer. Applies to both images and video frames.
  **Watch `--ink` with `--blend overlay`:** with the overlay formula used
  here, `--ink 0.5` is the exact mathematical no-op — it leaves every pixel
  unchanged, so the watermark is completely invisible, not just "medium
  strength." This is easy to hit by accident if you assume 0.5 is a safe
  middle value (it's the *0.32 default* that's a safe middle value). Stay
  clearly above or below 0.5 for a visible mark. Multiply doesn't have this
  trap in the middle of the range — there, smaller `--ink` means a darker
  mark and the no-op point is instead at the top of the range (`--ink 1.0`).

- **Content-adaptive placement** (`--adaptive`, CLI only — no equivalent
  toggle in `web/index.html`) — a lightweight pass (opencv's bundled Haar
  face detector, plus a local detail-energy signal that also catches other
  high-detail "main subject" areas: patterned clothing, foreground
  objects, on-image text) finds the regions of the frame where a clean
  inpaint-based removal is most likely to leave a visible seam, and stamps
  a second, denser grid on top exactly there (`--adaptive-infill-divisor`,
  default `2.0`, sets how much denser).
  For `--blend multiply|overlay`, it also darkens the mark further in
  those same regions (`--adaptive-strength`, default `0.6`, 0-1) — moving
  `--ink` further from that mode's own no-op point, the same one described
  above, never past it. Outside the detected regions the image is
  identical to the non-adaptive path — the boost is additive, not a
  global change. No extra model download or dependency: the face detector
  ships inside `opencv-python-headless`, already required for video.
  `--adaptive-preview some.png` (single images only) saves the detected
  mask itself (white = most boosted) so you can sanity-check or tune
  `--adaptive-detail-weight` (how much weight the general detail signal
  gets relative to face detection, default `0.5`) before committing to a
  batch run. `--face-cascade` swaps in a different Haar cascade XML if the
  bundled frontal-face one isn't a good fit for your subjects (e.g. a
  profile-face cascade for photos that aren't mostly front-facing).
  **Video:** by default (`--adaptive-track`, on) the mask is kept current
  across the whole clip instead of frozen at frame 0. wmcore.AdaptiveTracker
  runs once per decoded frame, entirely in the main process, separately
  from the worker pool that does the actual frame compositing: most frames
  it just carries the last detected mask forward with cheap optical flow on
  a downscaled copy (a moving subject or a panning/zooming camera is what
  this is for), and periodically (`--adaptive-redetect-seconds`, default
  `1.0`) it re-runs the real face/detail detection to correct the drift
  flow accumulates and pick up new subjects entering frame. A detected
  scene cut (see `--scene-cut-detect` above) skips the flow-warp for that
  transition and forces a fresh detection instead, since flow computed
  across a hard content change describes noise, not motion. Whatever the
  tracker currently holds when a `--jitter-refresh-seconds` segment
  boundary is reached is what that segment's mask gets built from, so the
  boost stays close to what's actually on screen for that segment rather
  than a fossil of frame 0. This adds no per-frame cost to the worker
  pool - only the once-per-segment mask rebuild that was already there.
  Pass `--no-adaptive-track` for the old behavior (detect once from frame
  0, reuse that snapshot for the entire video) if you need exact
  reproducibility with older output, or want to skip the extra per-frame
  optical-flow cost on a static/tripod shot where it buys nothing.
  **Scope:** `--adaptive` only changes the *visible* grid layer (its
  density and, for multiply/overlay, its darkness). It has no effect on
  either invisible mark - `lsb` still requires a lossless save and is
  destroyed by any recompression/resize, and `spread` keeps exactly the
  same JPEG-recompression/crop robustness and `--ss-key` caveats described in [Invisible marks](invisible-marks.md) either way. The biggest limitation of the invisible marks isn't
  changed by turning `--adaptive` on.

## Batch mode & performance

`--batch` processes a whole folder — images and videos can be mixed in the
same folder. Images are processed **in parallel** across `--workers`
processes (default: your CPU count) with a live progress bar; each video is
still processed one at a time, but its own frames are parallelized
internally the same way. A failure on one file (corrupt image, unreadable
video) is reported and skipped rather than stopping the whole batch.

Every file in a batch gets its own jitter pattern (deterministically derived
from `--seed` + filename), so a fixed `--seed` still gives you reproducible
output without every file in the batch sharing an identical watermark
pattern.
