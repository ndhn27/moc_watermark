# Watermark benchmark — `standard` suite
_2026-09-21T20:01:13+00:00 · 108 trials in 145.9 s · seed 20260919_

wmcore fingerprint `b4df979c2348` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss_id_rescale` detection** over gated attacks: 48/48 = 100.0% [92.6%-100.0%]; weakest gated attack `identity` at 100.0% (n=4).
- **`ss_id_rescale` unmarked-image FPR**: 0/12 = 0.0% (95% upper bound 26.5%).
- **`ss_id_rescale` runtime** on resized images it can recover: median of per-attack p50 = 2.2 s.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss_id_rescale` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| †flip_horizontal_resize_0.75 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 1.9 s | 2.0 s | n/a | n/a |  | no oracle geometry |
| †flip_vertical_resize_1.25 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 7.3 s | 7.4 s | n/a | n/a |  | no oracle geometry |
| identity | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 11 ms | 0.97 | n/a |  |  |
| resize_0.75 | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 1.0 s | 1.0 s | 0.80 | 0.0016 |  |  |
| resize_1.25 | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 1.7 s | 1.7 s | 0.80 | 0.0016 |  |  |

#### `ss_id_rescale` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| †flip_horizontal_resize_0.75 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 10.0 s | 10.0 s | n/a | n/a |  | no oracle geometry |
| †flip_vertical_resize_1.25 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 15.4 s | 16.6 s | n/a | n/a |  | no oracle geometry |
| identity | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 43 ms | 1.00 | n/a |  |  |
| resize_0.75 | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 2.3 s | 2.3 s | 0.83 | 0.0008 |  |  |
| resize_1.25 | 4 | 100.0% [51%–100%] | 0.0% | 0.000 | 0.000 | 2.4 s | 2.4 s | 0.83 | 0.0008 |  |  |

#### `ss_id_rescale` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| †flip_horizontal_resize_0.75 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 1.9 s | 2.4 s | n/a | n/a |  | no oracle geometry |
| †flip_vertical_resize_1.25 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 7.6 s | 7.9 s | n/a | n/a |  | no oracle geometry |
| identity | 4 | 100.0% [51%–100%] | 0.0% | 0.006 | 0.000 | 10 ms | 11 ms | 0.97 | n/a |  |  |
| resize_0.75 | 4 | 100.0% [51%–100%] | 0.0% | 0.010 | 0.000 | 1.0 s | 1.0 s | 0.80 | 0.0016 |  |  |
| resize_1.25 | 4 | 100.0% [51%–100%] | 0.0% | 0.007 | 0.000 | 1.7 s | 1.8 s | 0.79 | 0.0016 |  |  |

#### `ss_id_rescale` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| †flip_horizontal_resize_0.75 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 9.6 s | 9.9 s | n/a | n/a |  | no oracle geometry |
| †flip_vertical_resize_1.25 | 4 | 0.0% [0%–49%] | 0.0% | n/a | n/a | 14.2 s | 14.8 s | n/a | n/a |  | no oracle geometry |
| identity | 4 | 100.0% [51%–100%] | 0.0% | 0.005 | 0.000 | 36 ms | 40 ms | 1.00 | n/a |  |  |
| resize_0.75 | 4 | 100.0% [51%–100%] | 0.0% | 0.012 | 0.000 | 2.2 s | 2.2 s | 0.80 | 0.0008 |  |  |
| resize_1.25 | 4 | 100.0% [51%–100%] | 0.0% | 0.008 | 0.000 | 2.3 s | 2.4 s | 0.83 | 0.0008 |  |  |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss_id_rescale | identity | gradnoise 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | identity | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | identity | pink 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | identity | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | gradnoise 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | pink 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | gradnoise 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | pink 320×240 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss_id_rescale | 320×240 | 8 | 10 ms | 11 ms | 11 ms | 128 ms |  |
| decode:ss_id_rescale | 640×480 | 8 | 36 ms | 43 ms | 44 ms | 119 ms |  |
| embed:ss | 320×240 | 8 | 19 ms | 20 ms | 21 ms | 242 ms |  |
| embed:ss | 640×480 | 8 | 74 ms | 92 ms | 98 ms | 240 ms |  |
| rescale search [ss_id_rescale], mark found | 320×240 | 16 | 1.4 s | 1.7 s | 1.8 s | 19.3 s |  |
| rescale search [ss_id_rescale], mark found | 640×480 | 16 | 2.3 s | 2.4 s | 2.4 s | 8.8 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 320×240 | 6 | 5.0 s | 7.2 s | 7.2 s | 60.3 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 640×480 | 6 | 11.7 s | 13.9 s | 14.0 s | 38.0 s |  |
