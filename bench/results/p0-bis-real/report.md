# Watermark benchmark — `standard` suite
_2026-09-20T22:49:34+00:00 · 232 trials in 155.9 s · seed 20260919_

wmcore fingerprint `5434c60154df` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: real images from `/home/claude/work/real_photos`.

## Headline

- **`ss` detection** over gated attacks: 41/42 = 97.6% [87.7%-99.6%]; weakest gated attack `blur_1.0` at 0.0% (n=1).
- **`ss_rescale` detection** over gated attacks: 6/9 = 66.7% [35.4%-87.9%]; weakest gated attack `resize_0.75` at 0.0% (n=1).
- **`lsb` detection** over gated attacks: 7/7 = 100.0% [64.6%-100.0%]; weakest gated attack `identity` at 100.0% (n=1).
- **`lsb` unmarked-image FPR**: 3/14 = 21.4% (95% upper bound 50.8%).
- **`ss` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss_rescale` unmarked-image FPR**: 0/6 = 0.0% (95% upper bound 45.9%).
- **`ss` wrong-key acceptance**: 2/18 = 11.1% (95% upper bound 34.7%); exact payload recovered in 2/18.
- **`ss_rescale` runtime** on resized images it can recover: median of per-attack p50 = 5.1 s.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `lsb` · file 1282×1110 · payload `short` · PSNR 55.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †blur_1.0 | 1 | 0.0% [0%–79%] | 100.0% | 0.466 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †crop_unaligned_3 | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 29 ms | 29 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.000 | 0.000 | 34 ms | 34 ms |  |
| †jpeg_50 | 1 | 0.0% [0%–79%] | 100.0% | 0.500 | 0.533 | 35 ms | 35 ms | signal destroyed |
| †jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.500 | 0.550 | 43 ms | 43 ms | signal destroyed |
| †noise_5 | 1 | 0.0% [0%–79%] | 0.0% | 0.500 | 0.417 | 33 ms | 33 ms | signal destroyed |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 16 ms | 16 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 17 ms | 17 ms | no oracle geometry |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 49 ms | 49 ms | no oracle geometry |
| †webp_80 | 1 | 0.0% [0%–79%] | 0.0% | 0.500 | 0.517 | 32 ms | 32 ms | signal destroyed |

#### `lsb` · file 493×356 · payload `short` · PSNR 55.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †blur_1.0 | 1 | 0.0% [0%–79%] | 0.0% | 0.479 | 0.067 | 4 ms | 4 ms | signal degraded |
| †crop_unaligned_3 | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 4 ms | 4 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.000 | 0.000 | 4 ms | 4 ms |  |
| †jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.497 | 0.408 | 4 ms | 4 ms | signal destroyed |
| †jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.500 | 0.450 | 4 ms | 4 ms | signal destroyed |
| †noise_5 | 1 | 0.0% [0%–79%] | 0.0% | 0.497 | 0.400 | 4 ms | 4 ms | signal destroyed |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 2 ms | 2 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 2 ms | 2 ms | no oracle geometry |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 6 ms | 6 ms | no oracle geometry |
| †webp_80 | 1 | 0.0% [0%–79%] | 0.0% | 0.499 | 0.442 | 4 ms | 4 ms | signal destroyed |

#### `lsb` · file 512×480 · payload `short` · PSNR 55.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †blur_1.0 | 1 | 0.0% [0%–79%] | 0.0% | 0.447 | 0.000 | 5 ms | 5 ms | signal intact - decoder loses sync |
| †crop_unaligned_3 | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 5 ms | 5 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.000 | 0.000 | 5 ms | 5 ms |  |
| †jpeg_50 | 1 | 0.0% [0%–79%] | 100.0% | 0.501 | 0.508 | 8 ms | 8 ms | signal destroyed |
| †jpeg_75 | 1 | 0.0% [0%–79%] | 100.0% | 0.499 | 0.467 | 6 ms | 6 ms | signal destroyed |
| †noise_5 | 1 | 0.0% [0%–79%] | 0.0% | 0.500 | 0.550 | 5 ms | 5 ms | signal destroyed |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 3 ms | 3 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 3 ms | 3 ms | no oracle geometry |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 8 ms | 8 ms | no oracle geometry |
| †webp_80 | 1 | 0.0% [0%–79%] | 0.0% | 0.500 | 0.508 | 6 ms | 6 ms | signal destroyed |

#### `lsb` · file 512×512 · payload `short` · PSNR 55.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †blur_1.0 | 2 | 0.0% [0%–66%] | 0.0% | 0.486 | 0.267 | 6 ms | 6 ms | signal destroyed |
| †crop_unaligned_3 | 2 | 100.0% [34%–100%] | 0.0% | n/a | n/a | 5 ms | 5 ms |  |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.000 | 0.000 | 6 ms | 6 ms |  |
| †jpeg_50 | 2 | 0.0% [0%–66%] | 50.0% | 0.498 | 0.412 | 7 ms | 8 ms | signal destroyed |
| †jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.500 | 0.471 | 6 ms | 6 ms | signal destroyed |
| †noise_5 | 2 | 0.0% [0%–66%] | 0.0% | 0.499 | 0.442 | 6 ms | 6 ms | signal destroyed |
| †pipeline_resize_jpeg_crop | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 3 ms | 3 ms | no oracle geometry |
| †resize_0.75 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 3 ms | 4 ms | no oracle geometry |
| †resize_1.25 | 2 | 0.0% [0%–66%] | 50.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| †webp_80 | 2 | 0.0% [0%–66%] | 0.0% | 0.500 | 0.492 | 6 ms | 7 ms | signal destroyed |

#### `lsb` · file 640×480 · payload `short` · PSNR 56.0 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †blur_1.0 | 1 | 0.0% [0%–79%] | 0.0% | 0.493 | 0.200 | 6 ms | 6 ms | signal degraded |
| †crop_unaligned_3 | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 7 ms | 7 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.000 | 0.000 | 6 ms | 6 ms |  |
| †jpeg_50 | 1 | 0.0% [0%–79%] | 100.0% | 0.497 | 0.408 | 7 ms | 7 ms | signal destroyed |
| †jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.495 | 0.383 | 7 ms | 7 ms | signal destroyed |
| †noise_5 | 1 | 0.0% [0%–79%] | 0.0% | 0.497 | 0.433 | 6 ms | 6 ms | signal destroyed |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 4 ms | 4 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 4 ms | 4 ms | no oracle geometry |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 100.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| †webp_80 | 1 | 0.0% [0%–79%] | 100.0% | 0.496 | 0.358 | 7 ms | 7 ms | signal destroyed |

#### `lsb` · file 752×600 · payload `short` · PSNR 56.0 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.481 | 0.033 | 10 ms | 10 ms |  |
| †crop_unaligned_3 | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 10 ms | 10 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| †jpeg_50 | 1 | 0.0% [0%–79%] | 100.0% | 0.493 | 0.383 | 10 ms | 10 ms | signal destroyed |
| †jpeg_75 | 1 | 0.0% [0%–79%] | 100.0% | 0.494 | 0.375 | 11 ms | 11 ms | signal destroyed |
| †noise_5 | 1 | 0.0% [0%–79%] | 0.0% | 0.493 | 0.367 | 10 ms | 10 ms | signal destroyed |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 100.0% | n/a | n/a | 6 ms | 6 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 100.0% | n/a | n/a | 6 ms | 6 ms | no oracle geometry |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 100.0% | n/a | n/a | 16 ms | 16 ms | no oracle geometry |
| †webp_80 | 1 | 0.0% [0%–79%] | 100.0% | 0.496 | 0.392 | 10 ms | 10 ms | signal destroyed |

#### `ss` · file 1282×1110 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.053 | 0.000 | 183 ms | 183 ms |  |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 100.0% | n/a | n/a | 183 ms | 183 ms | no oracle geometry |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 185 ms | 185 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.011 | 0.000 | 189 ms | 189 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 186 ms | 186 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 183 ms | 183 ms |  |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 97 ms | 97 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.015 | 0.000 | 96 ms | 96 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 311 ms | 311 ms | signal intact - decoder loses sync |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 184 ms | 184 ms |  |

#### `ss` · file 493×356 · α=12 · payload `short` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.093 | 0.000 | 21 ms | 21 ms |  |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 21 ms | 21 ms | no oracle geometry |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.056 | 0.000 | 21 ms | 21 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 21 ms | 21 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 21 ms | 21 ms |  |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 12 ms | 12 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.060 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 32 ms | 32 ms | signal intact - decoder loses sync |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 21 ms | 21 ms |  |

#### `ss` · file 512×480 · α=12 · payload `short` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.026 | 0.000 | 29 ms | 29 ms |  |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.013 | 0.000 | 29 ms | 29 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms |  |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 16 ms | 16 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.011 | 0.000 | 16 ms | 16 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.009 | 0.000 | 45 ms | 45 ms | signal intact - decoder loses sync |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms |  |

#### `ss` · file 512×512 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 2 | 100.0% [34%–100%] | 0.0% | 0.069 | 0.000 | 31 ms | 31 ms |  |
| †crop_unaligned_3 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 32 ms | 32 ms |  |
| jpeg_50 | 2 | 100.0% [34%–100%] | 0.0% | 0.032 | 0.000 | 31 ms | 32 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.028 | 0.000 | 31 ms | 32 ms |  |
| noise_5 | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms |  |
| †pipeline_resize_jpeg_crop | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 17 ms | 17 ms | no oracle geometry |
| †resize_0.75 | 2 | 0.0% [0%–66%] | 0.0% | 0.038 | 0.000 | 18 ms | 18 ms | signal intact - decoder loses sync |
| †resize_1.25 | 2 | 0.0% [0%–66%] | 0.0% | 0.030 | 0.000 | 48 ms | 48 ms | signal intact - decoder loses sync |
| webp_80 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 31 ms | 32 ms |  |

#### `ss` · file 640×480 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 1 | 0.0% [0%–79%] | 0.0% | 0.202 | 0.000 | 38 ms | 38 ms | signal intact - decoder loses sync |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 36 ms | 36 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.141 | 0.000 | 36 ms | 36 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.128 | 0.000 | 36 ms | 36 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.126 | 0.000 | 37 ms | 37 ms |  |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.146 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.131 | 0.000 | 57 ms | 57 ms | signal intact - decoder loses sync |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.127 | 0.000 | 36 ms | 36 ms |  |

#### `ss` · file 752×600 · α=12 · payload `short` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.136 | 0.000 | 53 ms | 53 ms |  |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 53 ms | 53 ms | no oracle geometry |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 53 ms | 53 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.059 | 0.000 | 54 ms | 54 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 54 ms | 54 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 53 ms | 53 ms |  |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.062 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.047 | 0.000 | 83 ms | 83 ms | signal intact - decoder loses sync |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.041 | 0.000 | 54 ms | 54 ms |  |

#### `ss_rescale` · file 1282×1110 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 190 ms | 190 ms | 1.00 | n/a |  |  |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 10.7 s | 10.7 s | n/a | n/a | 1 | no oracle geometry |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.015 | 0.000 | 4.8 s | 4.8 s | 0.79 | 0.0001 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 5.1 s | 5.1 s | 0.78 | 0.0001 |  |  |

#### `ss_rescale` · file 512×512 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 32 ms | 32 ms | 1.00 | n/a |  |  |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 9.8 s | 9.8 s | n/a | n/a |  | no oracle geometry |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.066 | 0.000 | 9.8 s | 9.8 s | 0.78 | 0.0010 |  |  |
| resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 10.5 s | 10.5 s | n/a | n/a | 1 | signal intact - decoder loses sync |

#### `ss_rescale` · file 640×480 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms | 1.00 | n/a |  |  |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 8.7 s | 8.7 s | n/a | n/a |  | no oracle geometry |
| resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.146 | 0.000 | 9.6 s | 9.6 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.131 | 0.000 | 10.2 s | 10.2 s | n/a | n/a | 1 | signal intact - decoder loses sync |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | lsb | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | lsb | identity | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | lsb | identity | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | lsb | identity | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | lsb | identity | file 640×480 | 1 | 1 | 100.0% (≤100.0%) | — |
| unmarked image | lsb | identity | file 752×600 | 1 | 1 | 100.0% (≤100.0%) | — |
| unmarked image | lsb | jpeg_75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | lsb | jpeg_75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | lsb | jpeg_75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | lsb | jpeg_75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | lsb | jpeg_75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | lsb | jpeg_75 | file 752×600 | 1 | 1 | 100.0% (≤100.0%) | — |
| unmarked image | ss | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | identity | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | identity | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | identity | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | identity | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | identity | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | jpeg_75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | resize_0.75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss | resize_1.25 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | file 512×512 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | file 512×512 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | file 512×512 | 1 | 0 | 0.0% (≤97.5%) | — |
| marked, wrong key | ss | identity | file 1282×1110 | 3 | 1 | 33.3% (≤90.6%) | 1 |
| marked, wrong key | ss | identity | file 512×512 | 3 | 0 | 0.0% (≤70.8%) | 0 |
| marked, wrong key | ss | identity | file 640×480 | 3 | 0 | 0.0% (≤70.8%) | 0 |
| marked, wrong key | ss | jpeg_75 | file 1282×1110 | 3 | 1 | 33.3% (≤90.6%) | 1 |
| marked, wrong key | ss | jpeg_75 | file 512×512 | 3 | 0 | 0.0% (≤70.8%) | 0 |
| marked, wrong key | ss | jpeg_75 | file 640×480 | 3 | 0 | 0.0% (≤70.8%) | 0 |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:lsb | 493×356 | 1 | 4 ms | 4 ms | 4 ms | 22 ms |  |
| decode:lsb | 512×480 | 1 | 5 ms | 5 ms | 5 ms | 21 ms |  |
| decode:lsb | 512×512 | 2 | 6 ms | 6 ms | 6 ms | 23 ms |  |
| decode:lsb | 640×480 | 1 | 6 ms | 6 ms | 6 ms | 21 ms |  |
| decode:lsb | 752×600 | 1 | 10 ms | 10 ms | 10 ms | 22 ms |  |
| decode:lsb | 1282×1110 | 1 | 34 ms | 34 ms | 34 ms | 24 ms |  |
| decode:ss | 493×356 | 1 | 20 ms | 20 ms | 20 ms | 116 ms |  |
| decode:ss | 512×480 | 1 | 29 ms | 29 ms | 29 ms | 119 ms |  |
| decode:ss | 512×512 | 2 | 32 ms | 32 ms | 32 ms | 121 ms |  |
| decode:ss | 640×480 | 1 | 36 ms | 36 ms | 36 ms | 118 ms |  |
| decode:ss | 752×600 | 1 | 53 ms | 53 ms | 53 ms | 117 ms |  |
| decode:ss | 1282×1110 | 1 | 185 ms | 185 ms | 185 ms | 130 ms |  |
| decode:ss_rescale | 512×512 | 1 | 32 ms | 32 ms | 32 ms | 121 ms |  |
| decode:ss_rescale | 640×480 | 1 | 35 ms | 35 ms | 35 ms | 115 ms |  |
| decode:ss_rescale | 1282×1110 | 1 | 190 ms | 190 ms | 190 ms | 133 ms |  |
| embed:lsb | 493×356 | 1 | 6 ms | 6 ms | 6 ms | 33 ms |  |
| embed:lsb | 512×480 | 1 | 8 ms | 8 ms | 8 ms | 33 ms |  |
| embed:lsb | 512×512 | 2 | 9 ms | 9 ms | 9 ms | 34 ms |  |
| embed:lsb | 640×480 | 1 | 11 ms | 11 ms | 11 ms | 34 ms |  |
| embed:lsb | 752×600 | 1 | 16 ms | 16 ms | 16 ms | 35 ms |  |
| embed:lsb | 1282×1110 | 1 | 68 ms | 68 ms | 68 ms | 48 ms |  |
| embed:ss | 493×356 | 1 | 36 ms | 36 ms | 36 ms | 208 ms |  |
| embed:ss | 512×480 | 1 | 51 ms | 51 ms | 51 ms | 207 ms |  |
| embed:ss | 512×512 | 2 | 56 ms | 57 ms | 57 ms | 215 ms |  |
| embed:ss | 640×480 | 1 | 64 ms | 64 ms | 64 ms | 209 ms |  |
| embed:ss | 752×600 | 1 | 95 ms | 95 ms | 95 ms | 212 ms |  |
| embed:ss | 1282×1110 | 1 | 446 ms | 446 ms | 446 ms | 313 ms |  |
| rescale search, mark found | 512×512 | 1 | 9.8 s | 9.8 s | 9.8 s | 66.8 s |  |
| rescale search, mark found | 1282×1110 | 2 | 5.0 s | 5.1 s | 5.1 s | 4.2 s |  |
| rescale search, mark missed | 512×512 | 1 | 10.5 s | 10.5 s | 10.5 s | 25.6 s | 1 |
| rescale search, mark missed | 640×480 | 2 | 9.9 s | 10.1 s | 10.2 s | 38.4 s | 1 |
| rescale search, unmarked (nothing to find) | 512×512 | 3 | 10.3 s | 10.3 s | 10.3 s | 39.5 s | 2 |
| rescale search, unmarked (nothing to find) | 1282×1110 | 3 | 10.4 s | 10.5 s | 10.5 s | 7.3 s | 3 |
