# Watermark benchmark — `standard` suite
_2026-09-20T17:12:49+00:00 · 24 trials in 163.1 s · seed 20260919_

wmcore fingerprint `cd5b47394d21` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss_rescale` unmarked-image FPR**: 0/6 = 0.0% (95% upper bound 45.9%).

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss_rescale` · gradnoise 640×480 · α=12 · payload `short` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| †pipeline_heavy_repost | 3 | 0.0% [0%–56%] | 0.0% | n/a | n/a | 6.7 s | 6.7 s | n/a | n/a |  | no oracle geometry |
| †pipeline_resize_jpeg_crop | 3 | 0.0% [0%–56%] | 0.0% | n/a | n/a | 8.9 s | 9.5 s | n/a | n/a |  | no oracle geometry |

#### `ss_rescale` · pink 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| †pipeline_heavy_repost | 3 | 0.0% [0%–56%] | 0.0% | n/a | n/a | 6.5 s | 6.6 s | n/a | n/a |  | no oracle geometry |
| †pipeline_resize_jpeg_crop | 3 | 0.0% [0%–56%] | 0.0% | n/a | n/a | 8.9 s | 9.2 s | n/a | n/a |  | no oracle geometry |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss_rescale | identity | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | gradnoise 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | pink 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| embed:ss | 640×480 | 6 | 76 ms | 82 ms | 82 ms | 246 ms |  |
| rescale search, unmarked (nothing to find) | 640×480 | 6 | 11.5 s | 13.8 s | 13.8 s | 37.4 s |  |
