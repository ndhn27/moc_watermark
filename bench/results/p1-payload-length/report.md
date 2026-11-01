# Watermark benchmark — `standard` suite
_2026-09-20T21:13:33+00:00 · 592 trials in 51.5 s · seed 20260919_

wmcore fingerprint `44c81cd9c7ca` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss` detection** over gated attacks: 317/320 = 99.1% [97.3%-99.7%]; weakest gated attack `blur_1.0` at 87.5% (n=8).
- **`ss` unmarked-image FPR**: 0/8 = 0.0% (95% upper bound 36.9%).
- **`ss` wrong-key acceptance**: 6/8 = 75.0% (95% upper bound 96.8%); exact payload recovered in 6/8.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · gradnoise 640×480 · α=12 · payload `id` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 38 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 38 ms |  |
| †jpeg_30 | 8 | 50.0% [22%–78%] | 12.5% | 0.088 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 43 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 39 ms |  |
| †noise_10 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 38 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 39 ms |  |
| †resize_0.75 | 8 | 0.0% [0%–32%] | 0.0% | 0.000 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |

#### `ss` · gradnoise 640×480 · α=12 · payload `long` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 38 ms |  |
| †jpeg_30 | 8 | 50.0% [22%–78%] | 0.0% | 0.082 | 0.000 | 39 ms | 41 ms | signal intact - decoder loses sync |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 39 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 39 ms |  |
| †noise_10 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |
| †resize_0.75 | 8 | 0.0% [0%–32%] | 0.0% | 0.000 | 0.000 | 20 ms | 21 ms | signal intact - decoder loses sync |

#### `ss` · gradnoise 640×480 · α=12 · payload `medium` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 41 ms |  |
| †jpeg_30 | 8 | 50.0% [22%–78%] | 0.0% | 0.085 | 0.000 | 39 ms | 41 ms | signal intact - decoder loses sync |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 39 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 41 ms |  |
| †noise_10 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 41 ms |  |
| †resize_0.75 | 8 | 0.0% [0%–32%] | 0.0% | 0.000 | 0.000 | 20 ms | 21 ms | signal intact - decoder loses sync |

#### `ss` · gradnoise 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 39 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 39 ms |  |
| †jpeg_30 | 8 | 100.0% [68%–100%] | 0.0% | 0.083 | 0.000 | 39 ms | 39 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 38 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms |  |
| †noise_10 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 38 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 39 ms |  |
| †resize_0.75 | 8 | 0.0% [0%–32%] | 0.0% | 0.000 | 0.000 | 20 ms | 21 ms | signal intact - decoder loses sync |

#### `ss` · pink 640×480 · α=12 · payload `id` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 87.5% [53%–98%] | 0.0% | 0.018 | 0.000 | 39 ms | 41 ms | signal intact - decoder loses sync |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 38 ms | 38 ms |  |
| †jpeg_30 | 8 | 87.5% [53%–98%] | 0.0% | 0.108 | 0.000 | 40 ms | 45 ms | signal intact - decoder loses sync |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.006 | 0.000 | 38 ms | 40 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 38 ms | 41 ms |  |
| †noise_10 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 38 ms | 39 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 39 ms | 40 ms |  |
| †resize_0.75 | 8 | 0.0% [0%–32%] | 0.0% | 0.007 | 0.000 | 20 ms | 21 ms | signal intact - decoder loses sync |

#### `ss` · pink 640×480 · α=12 · payload `long` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 87.5% [53%–98%] | 0.0% | 0.018 | 0.000 | 38 ms | 39 ms | signal intact - decoder loses sync |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 38 ms | 39 ms |  |
| †jpeg_30 | 8 | 62.5% [31%–86%] | 12.5% | 0.099 | 0.001 | 39 ms | 40 ms | signal intact - decoder loses sync |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.006 | 0.000 | 37 ms | 38 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 38 ms | 39 ms |  |
| †noise_10 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 37 ms | 38 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 38 ms | 42 ms |  |
| †resize_0.75 | 8 | 0.0% [0%–32%] | 0.0% | 0.007 | 0.000 | 20 ms | 21 ms | signal intact - decoder loses sync |

#### `ss` · pink 640×480 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 100.0% [68%–100%] | 0.0% | 0.017 | 0.000 | 38 ms | 39 ms |  |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 38 ms | 39 ms |  |
| †jpeg_30 | 8 | 87.5% [53%–98%] | 0.0% | 0.105 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 38 ms | 39 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 39 ms | 39 ms |  |
| †noise_10 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 38 ms | 39 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.003 | 0.000 | 38 ms | 40 ms |  |
| †resize_0.75 | 8 | 0.0% [0%–32%] | 0.0% | 0.007 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |

#### `ss` · pink 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| blur_1.0 | 8 | 87.5% [53%–98%] | 0.0% | 0.020 | 0.000 | 38 ms | 39 ms | signal intact - decoder loses sync |
| identity | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 38 ms | 41 ms |  |
| †jpeg_30 | 8 | 100.0% [68%–100%] | 0.0% | 0.102 | 0.000 | 39 ms | 41 ms |  |
| jpeg_50 | 8 | 100.0% [68%–100%] | 0.0% | 0.006 | 0.000 | 38 ms | 39 ms |  |
| jpeg_60 | 8 | 100.0% [68%–100%] | 0.0% | 0.005 | 0.000 | 38 ms | 42 ms |  |
| †noise_10 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 38 ms | 39 ms |  |
| noise_5 | 8 | 100.0% [68%–100%] | 0.0% | 0.004 | 0.000 | 38 ms | 39 ms |  |
| †resize_0.75 | 8 | 0.0% [0%–32%] | 0.0% | 0.008 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss | identity | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | identity | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | jpeg_75 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_0.75 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss | resize_1.25 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| marked, wrong key | ss | identity | gradnoise 640×480 | 2 | 2 | 100.0% (≤100.0%) | 2 |
| marked, wrong key | ss | identity | pink 640×480 | 2 | 1 | 50.0% (≤98.7%) | 1 |
| marked, wrong key | ss | jpeg_75 | gradnoise 640×480 | 2 | 2 | 100.0% (≤100.0%) | 2 |
| marked, wrong key | ss | jpeg_75 | pink 640×480 | 2 | 1 | 50.0% (≤98.7%) | 1 |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss | 640×480 | 64 | 38 ms | 40 ms | 42 ms | 123 ms |  |
| embed:ss | 640×480 | 64 | 71 ms | 75 ms | 95 ms | 230 ms |  |
