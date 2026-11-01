# Watermark benchmark — `standard` suite
_2026-09-20T21:49:01+00:00 · 1056 trials in 38.3 s · seed 20260919_

wmcore fingerprint `e9a950ab80b7` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss` detection** over gated attacks: 843/896 = 94.1% [92.3%-95.4%]; weakest gated attack `crop_top_64` at 0.0% (n=8).
- **`ss` unmarked-image FPR**: 0/16 = 0.0% (95% upper bound 20.6%).
- **`ss` wrong-key acceptance**: 4/16 = 25.0% (95% upper bound 52.4%); exact payload recovered in 4/16.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · gradnoise 320×240 · α=12 · payload `id` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 7 ms | 7 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 19 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 20 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 19 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 20 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 20 ms |  |

#### `ss` · gradnoise 320×240 · α=12 · payload `long` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 16 ms |  |
| crop_top_64 | 8 | 0.0% [0%–32%] | 0.0% | 0.000 | 0.000 | 7 ms | 12 ms | signal intact - decoder loses sync |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 16 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 16 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 16 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 16 ms |  |

#### `ss` · gradnoise 320×240 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 16 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 7 ms | 7 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 19 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 19 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 20 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 20 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 16 ms |  |

#### `ss` · gradnoise 320×240 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 7 ms | 7 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 19 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 19 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 19 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 20 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 19 ms |  |

#### `ss` · gradnoise 480×360 · α=12 · payload `id` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 24 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 16 ms | 17 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 23 ms | 24 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 24 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 24 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 23 ms | 23 ms |  |

#### `ss` · gradnoise 480×360 · α=12 · payload `long` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 16 ms | 17 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 22 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 23 ms | 24 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |

#### `ss` · gradnoise 480×360 · α=12 · payload `medium` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 23 ms | 24 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 16 ms | 18 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 24 ms |  |

#### `ss` · gradnoise 480×360 · α=12 · payload `short` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 23 ms | 24 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 16 ms | 17 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 23 ms | 24 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 22 ms | 23 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 23 ms | 23 ms |  |

#### `ss` · pink 320×240 · α=12 · payload `id` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.018 | 0.000 | 10 ms | 10 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 7 ms | 7 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 10 ms | 11 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 13 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 11 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 10 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 10 ms | 11 ms |  |

#### `ss` · pink 320×240 · α=12 · payload `long` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 12.5% [2%–47%] | 37.5% | 0.020 | 0.014 | 10 ms | 10 ms | signal intact - decoder loses sync |
| crop_top_64 | 8 | 0.0% [0%–32%] | 0.0% | 0.003 | 0.003 | 7 ms | 8 ms | signal intact - decoder loses sync |
| identity | 8 | 50.0% [22%–78%] | 12.5% | 0.004 | 0.002 | 10 ms | 10 ms | signal intact - decoder loses sync |
| jpeg_50 | 8 | 37.5% [14%–69%] | 12.5% | 0.007 | 0.003 | 10 ms | 11 ms | signal intact - decoder loses sync |
| jpeg_60 | 8 | 25.0% [7%–59%] | 25.0% | 0.005 | 0.003 | 10 ms | 10 ms | signal intact - decoder loses sync |
| jpeg_75 | 8 | 50.0% [22%–78%] | 12.5% | 0.004 | 0.002 | 10 ms | 10 ms | signal intact - decoder loses sync |
| noise_5 | 8 | 50.0% [22%–78%] | 12.5% | 0.004 | 0.003 | 10 ms | 10 ms | signal intact - decoder loses sync |

#### `ss` · pink 320×240 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 75.0% [41%–93%] | 12.5% | 0.021 | 0.002 | 10 ms | 10 ms | signal intact - decoder loses sync |
| crop_top_64 | 8 | 87.5% [53%–98%] | 0.0% | 0.004 | 0.001 | 7 ms | 8 ms | signal intact - decoder loses sync |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 10 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.007 | 0.000 | 10 ms | 11 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.006 | 0.000 | 10 ms | 12 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 10 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 10 ms |  |

#### `ss` · pink 320×240 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.021 | 0.000 | 10 ms | 10 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 7 ms | 9 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 11 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.007 | 0.000 | 10 ms | 12 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 11 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 10 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 11 ms |  |

#### `ss` · pink 480×360 · α=12 · payload `id` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.017 | 0.000 | 22 ms | 22 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 16 ms | 17 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 23 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 23 ms | 23 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 26 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 23 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 23 ms |  |

#### `ss` · pink 480×360 · α=12 · payload `long` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 75.0% [41%–93%] | 25.0% | 0.016 | 0.001 | 22 ms | 23 ms | signal intact - decoder loses sync |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 16 ms | 17 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 23 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 22 ms | 23 ms |  |
| jpeg_60 | 8 | 87.5% [53%–98%] | 12.5% | 0.004 | 0.000 | 22 ms | 22 ms | signal intact - decoder loses sync |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 23 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 22 ms | 23 ms |  |

#### `ss` · pink 480×360 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 87.5% [53%–98%] | 12.5% | 0.018 | 0.000 | 22 ms | 23 ms | signal intact - decoder loses sync |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.002 | 0.000 | 16 ms | 17 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 22 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 22 ms | 24 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 22 ms | 22 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 23 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 24 ms |  |

#### `ss` · pink 480×360 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.020 | 0.000 | 22 ms | 23 ms |  |
| crop_top_64 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 16 ms | 17 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 22 ms | 23 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 22 ms | 23 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 22 ms | 22 ms |  |
| jpeg_75 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 22 ms | 22 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 22 ms | 23 ms |  |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss | identity | gradnoise 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | identity | gradnoise 480×360 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | identity | pink 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | identity | pink 480×360 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | gradnoise 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | gradnoise 480×360 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | pink 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | pink 480×360 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | gradnoise 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | gradnoise 480×360 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | pink 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | pink 480×360 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | gradnoise 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | gradnoise 480×360 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | pink 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | pink 480×360 | 1 | 0 | 0.0% (≤97.5%) | — |
| marked, wrong key | ss | identity | gradnoise 320×240 | 2 | 0 | 0.0% (≤84.2%) | 0 |
| marked, wrong key | ss | identity | gradnoise 480×360 | 2 | 1 | 50.0% (≤98.7%) | 1 |
| marked, wrong key | ss | identity | pink 320×240 | 2 | 0 | 0.0% (≤84.2%) | 0 |
| marked, wrong key | ss | identity | pink 480×360 | 2 | 1 | 50.0% (≤98.7%) | 1 |
| marked, wrong key | ss | jpeg_75 | gradnoise 320×240 | 2 | 0 | 0.0% (≤84.2%) | 0 |
| marked, wrong key | ss | jpeg_75 | gradnoise 480×360 | 2 | 1 | 50.0% (≤98.7%) | 1 |
| marked, wrong key | ss | jpeg_75 | pink 320×240 | 2 | 0 | 0.0% (≤84.2%) | 0 |
| marked, wrong key | ss | jpeg_75 | pink 480×360 | 2 | 1 | 50.0% (≤98.7%) | 1 |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss | 320×240 | 64 | 10 ms | 19 ms | 19 ms | 129 ms |  |
| decode:ss | 480×360 | 64 | 22 ms | 23 ms | 24 ms | 129 ms |  |
| embed:ss | 320×240 | 64 | 17 ms | 22 ms | 27 ms | 219 ms |  |
| embed:ss | 480×360 | 64 | 40 ms | 42 ms | 42 ms | 230 ms |  |
