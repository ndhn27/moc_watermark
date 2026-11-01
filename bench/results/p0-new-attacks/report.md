# Watermark benchmark — `standard` suite
_2026-09-20T17:09:29+00:00 · 238 trials in 170.8 s · seed 20260919_

wmcore fingerprint `cd5b47394d21` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss` detection** over gated attacks: 24/24 = 100.0% [86.2%-100.0%]; weakest gated attack `identity` at 100.0% (n=4).
- **`ss_rescale` detection** over gated attacks: 16/16 = 100.0% [80.6%-100.0%]; weakest gated attack `identity` at 100.0% (n=4).
- **`ss` unmarked-image FPR**: 0/16 = 0.0% (95% upper bound 20.6%).
- **`ss_rescale` unmarked-image FPR**: 0/6 = 0.0% (95% upper bound 45.9%).
- **`ss` wrong-key acceptance**: 8/32 = 25.0% (95% upper bound 43.4%); exact payload recovered in 6/32.
- **`ss_rescale` runtime** on resized images it can recover: median of per-attack p50 = 2.2 s.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · gradnoise 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †avif_60 | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms |  |
| †crop_unaligned_1 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 39 ms | 39 ms | no oracle geometry |
| †crop_unaligned_15 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 36 ms | 39 ms | no oracle geometry |
| †crop_unaligned_3 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 38 ms | 38 ms | no oracle geometry |
| †crop_unaligned_7 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 38 ms | 40 ms | no oracle geometry |
| †flip_horizontal | 4 | 0.0% [0%–49%] | 25.0% | n/a | n/a | 39 ms | 40 ms | no oracle geometry |
| identity | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 39 ms |  |
| jpeg_75 | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 40 ms | 41 ms |  |
| †perspective_light | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 40 ms | 40 ms | no oracle geometry |
| †perspective_medium | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 39 ms | 40 ms | no oracle geometry |
| †pipeline_heavy_repost | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 13 ms | 13 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 22 ms | 22 ms | no oracle geometry |
| †resize_0.75 | 4 | 0.0% [0%–49%] | 0.0% | 0.000 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †rotate_1deg | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 40 ms | 42 ms | no oracle geometry |
| †rotate_2deg | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 41 ms | 43 ms | no oracle geometry |
| †rotate_3deg | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 41 ms | 42 ms | no oracle geometry |
| †rotate_5deg | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 41 ms | 42 ms | no oracle geometry |
| webp_80 | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 39 ms |  |

#### `ss` · pink 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †avif_60 | 4 | 100.0% [51%–100%] | 0.0% | 0.007 | 0.000 | 39 ms | 41 ms |  |
| †crop_unaligned_1 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 37 ms | 39 ms | no oracle geometry |
| †crop_unaligned_15 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 35 ms | 37 ms | no oracle geometry |
| †crop_unaligned_3 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 37 ms | 38 ms | no oracle geometry |
| †crop_unaligned_7 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 38 ms | 39 ms | no oracle geometry |
| †flip_horizontal | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 39 ms | 39 ms | no oracle geometry |
| identity | 4 | 100.0% [51%–100%] | 0.0% | 0.007 | 0.000 | 38 ms | 39 ms |  |
| jpeg_75 | 4 | 100.0% [51%–100%] | 0.0% | 0.008 | 0.000 | 38 ms | 44 ms |  |
| †perspective_light | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 39 ms | 39 ms | no oracle geometry |
| †perspective_medium | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 40 ms | 40 ms | no oracle geometry |
| †pipeline_heavy_repost | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 13 ms | 13 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 22 ms | 22 ms | no oracle geometry |
| †resize_0.75 | 4 | 0.0% [0%–49%] | 0.0% | 0.014 | 0.000 | 20 ms | 23 ms | signal intact - decoder loses sync |
| †rotate_1deg | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 37 ms | 39 ms | no oracle geometry |
| †rotate_2deg | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 40 ms | 42 ms | no oracle geometry |
| †rotate_3deg | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 41 ms | 47 ms | no oracle geometry |
| †rotate_5deg | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 41 ms | 42 ms | no oracle geometry |
| webp_80 | 4 | 100.0% [51%–100%] | 0.0% | 0.008 | 0.000 | 38 ms | 39 ms |  |

#### `ss_rescale` · gradnoise 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms | 1.00 | n/a |  |  |
| †pipeline_heavy_repost | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 6.4 s | 6.5 s | n/a | n/a | 4 | no oracle geometry |
| †pipeline_resize_jpeg_crop | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 6.3 s | 6.4 s | n/a | n/a | 4 | no oracle geometry |
| resize_0.75 | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 2.2 s | 2.2 s | 0.83 | 0.0008 |  |  |

#### `ss_rescale` · pink 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 4 | 100.0% [51%–100%] | 0.0% | 0.007 | 0.000 | 38 ms | 40 ms | 1.00 | n/a |  |  |
| †pipeline_heavy_repost | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 6.5 s | 6.5 s | n/a | n/a | 4 | no oracle geometry |
| †pipeline_resize_jpeg_crop | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 6.5 s | 6.5 s | n/a | n/a | 4 | no oracle geometry |
| resize_0.75 | 4 | 100.0% [51%–100%] | 0.0% | 0.014 | 0.000 | 2.2 s | 2.3 s | 0.79 | 0.0008 |  |  |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss | identity | gradnoise 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | identity | pink 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | jpeg_75 | gradnoise 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | jpeg_75 | pink 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | resize_0.75 | gradnoise 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | resize_0.75 | pink 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | resize_1.25 | gradnoise 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | resize_1.25 | pink 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | identity | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| marked, wrong key | ss | identity | gradnoise 640×480 | 8 | 1 | 12.5% (≤52.7%) | 1 |
| marked, wrong key | ss | identity | pink 640×480 | 8 | 4 | 50.0% (≤84.3%) | 3 |
| marked, wrong key | ss | jpeg_75 | gradnoise 640×480 | 8 | 0 | 0.0% (≤36.9%) | 0 |
| marked, wrong key | ss | jpeg_75 | pink 640×480 | 8 | 3 | 37.5% (≤75.5%) | 2 |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss | 640×480 | 8 | 39 ms | 39 ms | 40 ms | 125 ms |  |
| decode:ss_rescale | 640×480 | 8 | 39 ms | 41 ms | 41 ms | 125 ms |  |
| embed:ss | 640×480 | 8 | 71 ms | 73 ms | 74 ms | 231 ms |  |
| rescale search, mark found | 640×480 | 8 | 2.2 s | 2.2 s | 2.3 s | 12.6 s |  |
| rescale search, unmarked (nothing to find) | 640×480 | 6 | 6.1 s | 6.4 s | 6.5 s | 19.7 s | 6 |
