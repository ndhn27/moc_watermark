# Watermark benchmark — `standard` suite
_2026-09-20T17:33:54+00:00 · 660 trials in 440.0 s · seed 20260919_

wmcore fingerprint `cd5b47394d21` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss` detection** over gated attacks: 96/96 = 100.0% [96.2%-100.0%]; weakest gated attack `avif_60` at 100.0% (n=12).
- **`ss_rescale` detection** over gated attacks: 48/48 = 100.0% [92.6%-100.0%]; weakest gated attack `identity` at 100.0% (n=12).
- **`ss` unmarked-image FPR**: 0/32 = 0.0% (95% upper bound 10.9%).
- **`ss_rescale` unmarked-image FPR**: 0/12 = 0.0% (95% upper bound 26.5%).
- **`ss` wrong-key acceptance**: 9/64 = 14.1% (95% upper bound 25.0%); exact payload recovered in 7/64.
- **`ss_rescale` runtime** on resized images it can recover: median of per-attack p50 = 1.9 s.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · gradnoise 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 30 ms | 33 ms |  |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 30 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 28 ms | 35 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 30 ms | 33 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 30 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 8.3% | n/a | n/a | 30 ms | 32 ms | no oracle geometry |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 30 ms | 32 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 30 ms | 31 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 34 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 33 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 12 ms | 14 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 16 ms | 18 ms | no oracle geometry |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 17 ms | 18 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 32 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 30 ms | 33 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 30 ms | 31 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 30 ms | 34 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 29 ms | 32 ms |  |

#### `ss` · pink 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 32 ms |  |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 33 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 28 ms | 30 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 31 ms | 35 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 32 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 32 ms | no oracle geometry |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 31 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 33 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 33 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 33 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 12 ms | 14 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 17 ms | 18 ms | no oracle geometry |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.008 | 0.000 | 17 ms | 19 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 31 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 30 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 32 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 29 ms | 33 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 29 ms | 33 ms |  |

#### `ss_rescale` · gradnoise 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 29 ms | 35 ms | 1.00 | n/a |  |  |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 5.7 s | 5.9 s | n/a | n/a |  | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 6.4 s | 6.5 s | n/a | n/a | 12 | no oracle geometry |
| resize_0.75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 1.9 s | 1.9 s | 0.83 | 0.0008 |  |  |

#### `ss_rescale` · pink 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 29 ms | 31 ms | 1.00 | n/a |  |  |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 5.7 s | 5.9 s | n/a | n/a |  | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 6.2 s | 6.4 s | n/a | n/a | 12 | no oracle geometry |
| resize_0.75 | 12 | 100.0% [76%–100%] | 0.0% | 0.008 | 0.000 | 1.9 s | 2.2 s | 0.79 | 0.0008 |  |  |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss | identity | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss | identity | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss | jpeg_75 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss | jpeg_75 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss | resize_0.75 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss | resize_0.75 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss | resize_1.25 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss | resize_1.25 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | identity | gradnoise 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | identity | pink 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | resize_0.75 | gradnoise 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | resize_0.75 | pink 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | resize_1.25 | gradnoise 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | resize_1.25 | pink 640×480 | 2 | 0 | 0.0% (≤84.2%) | — |
| marked, wrong key | ss | identity | gradnoise 640×480 | 16 | 2 | 12.5% (≤38.3%) | 2 |
| marked, wrong key | ss | identity | pink 640×480 | 16 | 4 | 25.0% (≤52.4%) | 3 |
| marked, wrong key | ss | jpeg_75 | gradnoise 640×480 | 16 | 0 | 0.0% (≤20.6%) | 0 |
| marked, wrong key | ss | jpeg_75 | pink 640×480 | 16 | 3 | 18.8% (≤45.6%) | 2 |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss | 640×480 | 24 | 30 ms | 32 ms | 33 ms | 96 ms |  |
| decode:ss_rescale | 640×480 | 24 | 29 ms | 32 ms | 38 ms | 96 ms |  |
| embed:ss | 640×480 | 24 | 59 ms | 62 ms | 62 ms | 191 ms |  |
| rescale search, mark found | 640×480 | 24 | 1.9 s | 2.0 s | 2.3 s | 10.8 s |  |
| rescale search, unmarked (nothing to find) | 640×480 | 12 | 6.2 s | 6.3 s | 6.4 s | 20.5 s | 12 |
