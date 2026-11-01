# Watermark benchmark — `standard` suite
_2026-09-21T10:27:16+00:00 · 259 trials in 1455.7 s · seed 20260919_

wmcore fingerprint `b62d785325a9` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: real images from `/home/claude/realimgs`.

## Headline

- **`ss_rescale` detection** over gated attacks: 53/56 = 94.6% [85.4%-98.2%]; weakest gated attack `resize_0.62` at 0.0% (n=1).
- **`ss_id_rescale` detection** over gated attacks: 56/56 = 100.0% [93.6%-100.0%]; weakest gated attack `identity` at 100.0% (n=1).
- **`ss_or_id_rescale` detection** over gated attacks: 56/56 = 100.0% [93.6%-100.0%]; weakest gated attack `identity` at 100.0% (n=1).
- **`ss_rescale` unmarked-image FPR**: 0/21 = 0.0% (95% upper bound 16.1%).
- **`ss_id_rescale` unmarked-image FPR**: 0/21 = 0.0% (95% upper bound 16.1%).
- **`ss_or_id_rescale` unmarked-image FPR**: 0/21 = 0.0% (95% upper bound 16.1%).
- **`ss_rescale` runtime** on resized images it can recover: median of per-attack p50 = 2.2 s.
- **`ss_id_rescale` runtime** on resized images it can recover: median of per-attack p50 = 2.2 s.
- **`ss_or_id_rescale` runtime** on resized images it can recover: median of per-attack p50 = 2.2 s.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss_id_rescale` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 161 ms | 161 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.105 | 0.000 | 4.6 s | 4.6 s | 0.75 | 0.0004 |  |  |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.031 | 0.000 | 4.5 s | 4.5 s | 0.81 | 0.0002 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.011 | 0.000 | 4.6 s | 4.6 s | 0.83 | 0.0001 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.022 | 0.000 | 4.5 s | 4.5 s | 0.82 | 0.0001 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 4.7 s | 4.7 s | 0.82 | 0.0006 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 4.8 s | 4.8 s | 0.81 | 0.0001 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 5.0 s | 5.0 s | 0.82 | 0.0003 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 5.0 s | 5.0 s | 0.81 | 0.0004 |  |  |

#### `ss_id_rescale` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 2.4 s | 2.4 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.087 | 0.000 | 1.6 s | 1.6 s | 0.77 | 0.0001 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.064 | 0.000 | 1.8 s | 1.8 s | 0.77 | 0.0003 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.074 | 0.000 | 1.8 s | 1.8 s | 0.75 | 0.0003 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.064 | 0.000 | 2.1 s | 2.1 s | 0.75 | 0.0003 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.059 | 0.000 | 11.2 s | 11.2 s | 0.75 | 0.0014 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.063 | 0.000 | 12.0 s | 12.0 s | 0.74 | 0.0013 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.059 | 0.000 | 12.7 s | 12.7 s | 0.73 | 0.0003 |  |  |

#### `ss_id_rescale` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 1.7 s | 1.7 s | 0.81 | 0.0010 |  |  |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.021 | 0.000 | 2.1 s | 2.1 s | 0.80 | 0.0024 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.008 | 0.000 | 2.1 s | 2.1 s | 0.77 | 0.0010 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.018 | 0.000 | 2.1 s | 2.1 s | 0.76 | 0.0010 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.1 s | 2.1 s | 0.75 | 0.0005 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0010 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.2 s | 2.2 s | 0.81 | 0.0007 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.1 s | 2.1 s | 0.79 | 0.0010 |  |  |

#### `ss_id_rescale` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 32 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 2 | 50.0% [9%–91%] | 0.0% | 0.119 | 0.000 | 3.8 s | 5.6 s | 0.80 | 0.0010 |  | signal intact - decoder loses sync |
| resize_0.62 | 2 | 100.0% [34%–100%] | 0.0% | 0.064 | 0.000 | 2.1 s | 2.1 s | 0.75 | 0.0024 |  |  |
| resize_0.75 | 2 | 100.0% [34%–100%] | 0.0% | 0.039 | 0.000 | 9.7 s | 9.7 s | 0.77 | 0.0010 |  |  |
| resize_0.75_jpeg85 | 2 | 100.0% [34%–100%] | 0.0% | 0.046 | 0.000 | 10.7 s | 11.6 s | 0.77 | 0.0010 |  |  |
| resize_0.9 | 2 | 100.0% [34%–100%] | 0.0% | 0.034 | 0.000 | 6.8 s | 11.0 s | 0.76 | 0.0005 |  |  |
| resize_1.25 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 2.2 s | 2.2 s | 0.77 | 0.0010 |  |  |
| resize_1.4_jpeg85 | 2 | 100.0% [34%–100%] | 0.0% | 0.034 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0007 |  |  |
| resize_1.5 | 2 | 100.0% [34%–100%] | 0.0% | 0.031 | 0.000 | 2.2 s | 2.2 s | 0.79 | 0.0010 |  |  |

#### `ss_id_rescale` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.221 | 0.000 | 4.7 s | 4.7 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.171 | 0.000 | 2.1 s | 2.1 s | 0.77 | 0.0003 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.133 | 0.000 | 2.1 s | 2.1 s | 0.78 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.142 | 0.000 | 2.1 s | 2.1 s | 0.77 | 0.0008 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.130 | 0.000 | 2.1 s | 2.1 s | 0.79 | 0.0008 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.120 | 0.000 | 2.1 s | 2.1 s | 0.79 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.133 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0008 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.126 | 0.000 | 2.2 s | 2.2 s | 0.77 | 0.0008 |  |  |

#### `ss_id_rescale` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 51 ms | 51 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.163 | 0.000 | 7.0 s | 7.0 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.093 | 0.000 | 2.2 s | 2.2 s | 0.73 | 0.0012 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.061 | 0.000 | 2.2 s | 2.2 s | 0.75 | 0.0007 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.076 | 0.000 | 2.2 s | 2.2 s | 0.74 | 0.0007 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.053 | 0.000 | 2.2 s | 2.2 s | 0.75 | 0.0004 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 2.3 s | 2.3 s | 0.77 | 0.0007 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.054 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0005 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.047 | 0.000 | 2.3 s | 2.3 s | 0.79 | 0.0007 |  |  |

#### `ss_or_id_rescale` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 168 ms | 168 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.105 | 0.000 | 4.8 s | 4.8 s | 0.75 | 0.0004 |  |  |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.031 | 0.000 | 4.6 s | 4.6 s | 0.81 | 0.0002 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.011 | 0.000 | 4.6 s | 4.6 s | 0.83 | 0.0001 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.022 | 0.000 | 4.6 s | 4.6 s | 0.82 | 0.0001 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 4.6 s | 4.6 s | 0.82 | 0.0006 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 4.9 s | 4.9 s | 0.81 | 0.0001 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 5.0 s | 5.0 s | 0.82 | 0.0003 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 5.2 s | 5.2 s | 0.81 | 0.0004 |  |  |

#### `ss_or_id_rescale` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 2.5 s | 2.5 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.087 | 0.000 | 1.7 s | 1.7 s | 0.77 | 0.0001 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.064 | 0.000 | 1.9 s | 1.9 s | 0.77 | 0.0003 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.074 | 0.000 | 1.8 s | 1.8 s | 0.75 | 0.0003 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.064 | 0.000 | 2.1 s | 2.1 s | 0.75 | 0.0003 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.059 | 0.000 | 12.0 s | 12.0 s | 0.75 | 0.0014 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.063 | 0.000 | 11.8 s | 11.8 s | 0.74 | 0.0013 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.059 | 0.000 | 12.8 s | 12.8 s | 0.73 | 0.0003 |  |  |

#### `ss_or_id_rescale` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 1.7 s | 1.7 s | 0.81 | 0.0010 |  |  |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.021 | 0.000 | 2.0 s | 2.0 s | 0.80 | 0.0024 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.008 | 0.000 | 2.1 s | 2.1 s | 0.77 | 0.0010 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.018 | 0.000 | 2.1 s | 2.1 s | 0.76 | 0.0010 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.0 s | 2.0 s | 0.75 | 0.0005 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 2.0 s | 2.0 s | 0.78 | 0.0010 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.2 s | 2.2 s | 0.81 | 0.0007 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.2 s | 2.2 s | 0.79 | 0.0010 |  |  |

#### `ss_or_id_rescale` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 32 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 2 | 50.0% [9%–91%] | 0.0% | 0.119 | 0.000 | 3.8 s | 5.7 s | 0.80 | 0.0010 |  | signal intact - decoder loses sync |
| resize_0.62 | 2 | 100.0% [34%–100%] | 0.0% | 0.064 | 0.000 | 2.1 s | 2.1 s | 0.75 | 0.0024 |  |  |
| resize_0.75 | 2 | 100.0% [34%–100%] | 0.0% | 0.039 | 0.000 | 9.7 s | 9.7 s | 0.77 | 0.0010 |  |  |
| resize_0.75_jpeg85 | 2 | 100.0% [34%–100%] | 0.0% | 0.046 | 0.000 | 10.5 s | 11.3 s | 0.77 | 0.0010 |  |  |
| resize_0.9 | 2 | 100.0% [34%–100%] | 0.0% | 0.034 | 0.000 | 6.7 s | 10.7 s | 0.76 | 0.0005 |  |  |
| resize_1.25 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 2.1 s | 2.1 s | 0.77 | 0.0010 |  |  |
| resize_1.4_jpeg85 | 2 | 100.0% [34%–100%] | 0.0% | 0.034 | 0.000 | 2.1 s | 2.2 s | 0.78 | 0.0007 |  |  |
| resize_1.5 | 2 | 100.0% [34%–100%] | 0.0% | 0.031 | 0.000 | 2.2 s | 2.3 s | 0.79 | 0.0010 |  |  |

#### `ss_or_id_rescale` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.221 | 0.000 | 4.7 s | 4.7 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.171 | 0.000 | 2.1 s | 2.1 s | 0.77 | 0.0003 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.133 | 0.000 | 2.1 s | 2.1 s | 0.78 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.142 | 0.000 | 2.3 s | 2.3 s | 0.77 | 0.0008 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.130 | 0.000 | 2.3 s | 2.3 s | 0.79 | 0.0008 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.120 | 0.000 | 2.2 s | 2.2 s | 0.79 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.133 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0008 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.126 | 0.000 | 2.2 s | 2.2 s | 0.77 | 0.0008 |  |  |

#### `ss_or_id_rescale` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 52 ms | 52 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.163 | 0.000 | 7.0 s | 7.0 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.093 | 0.000 | 2.2 s | 2.2 s | 0.73 | 0.0012 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.061 | 0.000 | 2.2 s | 2.2 s | 0.75 | 0.0007 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.076 | 0.000 | 2.2 s | 2.2 s | 0.74 | 0.0007 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.053 | 0.000 | 2.2 s | 2.2 s | 0.75 | 0.0004 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 2.3 s | 2.3 s | 0.77 | 0.0007 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.054 | 0.000 | 2.3 s | 2.3 s | 0.78 | 0.0005 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.047 | 0.000 | 2.3 s | 2.3 s | 0.79 | 0.0007 |  |  |

#### `ss_rescale` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 160 ms | 160 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.105 | 0.000 | 4.6 s | 4.6 s | 0.75 | 0.0004 |  |  |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.031 | 0.000 | 4.5 s | 4.5 s | 0.81 | 0.0002 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.011 | 0.000 | 4.7 s | 4.7 s | 0.83 | 0.0001 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.022 | 0.000 | 4.6 s | 4.6 s | 0.82 | 0.0001 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 4.6 s | 4.6 s | 0.82 | 0.0006 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 4.9 s | 4.9 s | 0.81 | 0.0001 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 5.0 s | 5.0 s | 0.82 | 0.0003 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 5.0 s | 5.0 s | 0.81 | 0.0004 |  |  |

#### `ss_rescale` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 22 ms | 22 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 2.5 s | 2.5 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.087 | 0.000 | 1.7 s | 1.7 s | 0.77 | 0.0001 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.064 | 0.000 | 1.9 s | 1.9 s | 0.77 | 0.0003 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.074 | 0.000 | 1.8 s | 1.8 s | 0.75 | 0.0003 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.064 | 0.000 | 2.1 s | 2.1 s | 0.75 | 0.0003 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.059 | 0.000 | 11.2 s | 11.2 s | 0.75 | 0.0014 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.063 | 0.000 | 12.0 s | 12.0 s | 0.74 | 0.0013 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.059 | 0.000 | 15.3 s | 15.3 s | 0.73 | 0.0003 |  |  |

#### `ss_rescale` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 27 ms | 27 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 1.7 s | 1.7 s | 0.81 | 0.0010 |  |  |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.021 | 0.000 | 2.0 s | 2.0 s | 0.80 | 0.0024 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.008 | 0.000 | 2.1 s | 2.1 s | 0.77 | 0.0010 |  |  |
| resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.018 | 0.000 | 9.6 s | 9.6 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.2 s | 2.2 s | 0.75 | 0.0005 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0010 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.2 s | 2.2 s | 0.81 | 0.0007 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 2.1 s | 2.1 s | 0.79 | 0.0010 |  |  |

#### `ss_rescale` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 32 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 2 | 50.0% [9%–91%] | 0.0% | 0.119 | 0.000 | 3.9 s | 5.7 s | 0.80 | 0.0010 |  | signal intact - decoder loses sync |
| resize_0.62 | 2 | 100.0% [34%–100%] | 0.0% | 0.064 | 0.000 | 2.1 s | 2.1 s | 0.75 | 0.0024 |  |  |
| resize_0.75 | 2 | 100.0% [34%–100%] | 0.0% | 0.039 | 0.000 | 9.6 s | 9.8 s | 0.77 | 0.0010 |  |  |
| resize_0.75_jpeg85 | 2 | 100.0% [34%–100%] | 0.0% | 0.046 | 0.000 | 9.9 s | 10.2 s | 0.77 | 0.0010 |  |  |
| resize_0.9 | 2 | 100.0% [34%–100%] | 0.0% | 0.034 | 0.000 | 6.7 s | 10.8 s | 0.76 | 0.0005 |  |  |
| resize_1.25 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 2.2 s | 2.2 s | 0.77 | 0.0010 |  |  |
| resize_1.4_jpeg85 | 2 | 100.0% [34%–100%] | 0.0% | 0.034 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0007 |  |  |
| resize_1.5 | 2 | 100.0% [34%–100%] | 0.0% | 0.031 | 0.000 | 2.1 s | 2.2 s | 0.79 | 0.0010 |  |  |

#### `ss_rescale` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.221 | 0.000 | 4.7 s | 4.7 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.171 | 0.000 | 7.7 s | 7.7 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.133 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.142 | 0.000 | 9.4 s | 9.4 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.130 | 0.000 | 2.2 s | 2.2 s | 0.79 | 0.0008 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.120 | 0.000 | 2.2 s | 2.2 s | 0.79 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.133 | 0.000 | 2.3 s | 2.3 s | 0.78 | 0.0008 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.126 | 0.000 | 2.2 s | 2.2 s | 0.77 | 0.0008 |  |  |

#### `ss_rescale` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 53 ms | 53 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.163 | 0.000 | 7.0 s | 7.0 s | n/a | n/a |  | signal intact - decoder loses sync |
| resize_0.62 | 1 | 100.0% [21%–100%] | 0.0% | 0.093 | 0.000 | 2.2 s | 2.2 s | 0.73 | 0.0012 |  |  |
| resize_0.75 | 1 | 100.0% [21%–100%] | 0.0% | 0.061 | 0.000 | 2.2 s | 2.2 s | 0.75 | 0.0007 |  |  |
| resize_0.75_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.076 | 0.000 | 2.2 s | 2.2 s | 0.74 | 0.0007 |  |  |
| resize_0.9 | 1 | 100.0% [21%–100%] | 0.0% | 0.053 | 0.000 | 2.2 s | 2.2 s | 0.75 | 0.0004 |  |  |
| resize_1.25 | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 2.3 s | 2.3 s | 0.77 | 0.0007 |  |  |
| resize_1.4_jpeg85 | 1 | 100.0% [21%–100%] | 0.0% | 0.054 | 0.000 | 2.2 s | 2.2 s | 0.78 | 0.0005 |  |  |
| resize_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.047 | 0.000 | 2.3 s | 2.3 s | 0.79 | 0.0007 |  |  |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss_id_rescale | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | identity | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | identity | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | identity | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id_rescale | identity | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | identity | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | identity | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | identity | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | identity | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_or_id_rescale | identity | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | identity | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | identity | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | identity | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | resize_0.75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_0.75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_rescale | resize_1.25 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_rescale | resize_1.25 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss_id_rescale | 493×356 | 1 | 21 ms | 21 ms | 21 ms | 118 ms |  |
| decode:ss_id_rescale | 512×480 | 1 | 29 ms | 29 ms | 29 ms | 120 ms |  |
| decode:ss_id_rescale | 512×512 | 2 | 31 ms | 32 ms | 32 ms | 118 ms |  |
| decode:ss_id_rescale | 640×480 | 1 | 36 ms | 36 ms | 36 ms | 117 ms |  |
| decode:ss_id_rescale | 752×600 | 1 | 51 ms | 51 ms | 51 ms | 114 ms |  |
| decode:ss_id_rescale | 1282×1110 | 1 | 161 ms | 161 ms | 161 ms | 113 ms |  |
| decode:ss_or_id_rescale | 493×356 | 1 | 21 ms | 21 ms | 21 ms | 118 ms |  |
| decode:ss_or_id_rescale | 512×480 | 1 | 29 ms | 29 ms | 29 ms | 118 ms |  |
| decode:ss_or_id_rescale | 512×512 | 2 | 31 ms | 32 ms | 32 ms | 119 ms |  |
| decode:ss_or_id_rescale | 640×480 | 1 | 36 ms | 36 ms | 36 ms | 118 ms |  |
| decode:ss_or_id_rescale | 752×600 | 1 | 52 ms | 52 ms | 52 ms | 115 ms |  |
| decode:ss_or_id_rescale | 1282×1110 | 1 | 168 ms | 168 ms | 168 ms | 118 ms |  |
| decode:ss_rescale | 493×356 | 1 | 22 ms | 22 ms | 22 ms | 123 ms |  |
| decode:ss_rescale | 512×480 | 1 | 27 ms | 27 ms | 27 ms | 110 ms |  |
| decode:ss_rescale | 512×512 | 2 | 31 ms | 32 ms | 32 ms | 119 ms |  |
| decode:ss_rescale | 640×480 | 1 | 36 ms | 36 ms | 36 ms | 116 ms |  |
| decode:ss_rescale | 752×600 | 1 | 53 ms | 53 ms | 53 ms | 118 ms |  |
| decode:ss_rescale | 1282×1110 | 1 | 160 ms | 160 ms | 160 ms | 113 ms |  |
| embed:ss | 493×356 | 1 | 37 ms | 37 ms | 37 ms | 213 ms |  |
| embed:ss | 512×480 | 1 | 50 ms | 50 ms | 50 ms | 202 ms |  |
| embed:ss | 512×512 | 2 | 56 ms | 56 ms | 56 ms | 213 ms |  |
| embed:ss | 640×480 | 1 | 68 ms | 68 ms | 68 ms | 220 ms |  |
| embed:ss | 752×600 | 1 | 94 ms | 94 ms | 94 ms | 207 ms |  |
| embed:ss | 1282×1110 | 1 | 439 ms | 439 ms | 439 ms | 308 ms |  |
| rescale search [ss_id_rescale], mark found | 493×356 | 7 | 2.1 s | 12.5 s | 12.7 s | 23.8 s |  |
| rescale search [ss_id_rescale], mark found | 512×480 | 8 | 2.1 s | 2.2 s | 2.2 s | 12.6 s |  |
| rescale search [ss_id_rescale], mark found | 512×512 | 15 | 2.2 s | 11.5 s | 11.7 s | 20.6 s |  |
| rescale search [ss_id_rescale], mark found | 640×480 | 7 | 2.1 s | 2.2 s | 2.2 s | 8.6 s |  |
| rescale search [ss_id_rescale], mark found | 752×600 | 7 | 2.2 s | 2.3 s | 2.3 s | 6.0 s |  |
| rescale search [ss_id_rescale], mark found | 1282×1110 | 8 | 4.6 s | 5.0 s | 5.0 s | 4.8 s |  |
| rescale search [ss_id_rescale], mark missed | 493×356 | 1 | 2.4 s | 2.4 s | 2.4 s | 55.6 s |  |
| rescale search [ss_id_rescale], mark missed | 512×512 | 1 | 5.8 s | 5.8 s | 5.8 s | 88.3 s |  |
| rescale search [ss_id_rescale], mark missed | 640×480 | 1 | 4.7 s | 4.7 s | 4.7 s | 61.3 s |  |
| rescale search [ss_id_rescale], mark missed | 752×600 | 1 | 7.0 s | 7.0 s | 7.0 s | 62.2 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 493×356 | 3 | 8.8 s | 11.1 s | 11.3 s | 50.3 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 512×480 | 3 | 11.4 s | 13.5 s | 13.7 s | 46.3 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 512×512 | 6 | 12.1 s | 17.0 s | 18.0 s | 46.1 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 640×480 | 3 | 11.5 s | 13.5 s | 13.7 s | 37.5 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 752×600 | 3 | 13.6 s | 14.2 s | 14.3 s | 30.0 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 1282×1110 | 3 | 14.2 s | 20.2 s | 20.9 s | 10.0 s | 1 |
| rescale search [ss_or_id_rescale], mark found | 493×356 | 7 | 2.1 s | 12.6 s | 12.8 s | 24.7 s |  |
| rescale search [ss_or_id_rescale], mark found | 512×480 | 8 | 2.1 s | 2.2 s | 2.2 s | 12.5 s |  |
| rescale search [ss_or_id_rescale], mark found | 512×512 | 15 | 2.2 s | 11.2 s | 11.4 s | 20.6 s |  |
| rescale search [ss_or_id_rescale], mark found | 640×480 | 7 | 2.2 s | 2.3 s | 2.3 s | 9.2 s |  |
| rescale search [ss_or_id_rescale], mark found | 752×600 | 7 | 2.2 s | 2.3 s | 2.3 s | 6.0 s |  |
| rescale search [ss_or_id_rescale], mark found | 1282×1110 | 8 | 4.7 s | 5.1 s | 5.2 s | 4.8 s |  |
| rescale search [ss_or_id_rescale], mark missed | 493×356 | 1 | 2.5 s | 2.5 s | 2.5 s | 57.2 s |  |
| rescale search [ss_or_id_rescale], mark missed | 512×512 | 1 | 5.9 s | 5.9 s | 5.9 s | 89.4 s |  |
| rescale search [ss_or_id_rescale], mark missed | 640×480 | 1 | 4.7 s | 4.7 s | 4.7 s | 61.2 s |  |
| rescale search [ss_or_id_rescale], mark missed | 752×600 | 1 | 7.0 s | 7.0 s | 7.0 s | 62.0 s |  |
| rescale search [ss_or_id_rescale], unmarked (nothing to find) | 493×356 | 3 | 9.0 s | 10.7 s | 10.9 s | 51.2 s |  |
| rescale search [ss_or_id_rescale], unmarked (nothing to find) | 512×480 | 3 | 11.4 s | 13.2 s | 13.4 s | 46.5 s |  |
| rescale search [ss_or_id_rescale], unmarked (nothing to find) | 512×512 | 6 | 12.1 s | 14.2 s | 14.2 s | 46.3 s |  |
| rescale search [ss_or_id_rescale], unmarked (nothing to find) | 640×480 | 3 | 11.7 s | 13.4 s | 13.6 s | 38.1 s |  |
| rescale search [ss_or_id_rescale], unmarked (nothing to find) | 752×600 | 3 | 13.6 s | 14.3 s | 14.3 s | 30.2 s |  |
| rescale search [ss_or_id_rescale], unmarked (nothing to find) | 1282×1110 | 3 | 14.3 s | 20.3 s | 20.9 s | 10.0 s | 1 |
| rescale search, mark found | 493×356 | 7 | 2.1 s | 14.3 s | 15.3 s | 25.0 s |  |
| rescale search, mark found | 512×480 | 7 | 2.1 s | 2.2 s | 2.2 s | 10.8 s |  |
| rescale search, mark found | 512×512 | 15 | 2.2 s | 10.5 s | 11.3 s | 20.4 s |  |
| rescale search, mark found | 640×480 | 5 | 2.2 s | 2.2 s | 2.3 s | 4.5 s |  |
| rescale search, mark found | 752×600 | 7 | 2.2 s | 2.3 s | 2.3 s | 6.0 s |  |
| rescale search, mark found | 1282×1110 | 8 | 4.7 s | 5.0 s | 5.0 s | 4.9 s |  |
| rescale search, mark missed | 493×356 | 1 | 2.5 s | 2.5 s | 2.5 s | 56.1 s |  |
| rescale search, mark missed | 512×480 | 1 | 9.6 s | 9.6 s | 9.6 s | 69.6 s |  |
| rescale search, mark missed | 512×512 | 1 | 5.9 s | 5.9 s | 5.9 s | 90.3 s |  |
| rescale search, mark missed | 640×480 | 3 | 7.7 s | 9.2 s | 9.4 s | 60.8 s |  |
| rescale search, mark missed | 752×600 | 1 | 7.0 s | 7.0 s | 7.0 s | 61.9 s |  |
| rescale search, unmarked (nothing to find) | 493×356 | 3 | 8.9 s | 10.8 s | 11.0 s | 50.9 s |  |
| rescale search, unmarked (nothing to find) | 512×480 | 3 | 11.5 s | 13.2 s | 13.4 s | 46.8 s |  |
| rescale search, unmarked (nothing to find) | 512×512 | 6 | 11.9 s | 14.2 s | 14.3 s | 45.4 s |  |
| rescale search, unmarked (nothing to find) | 640×480 | 3 | 11.6 s | 13.8 s | 14.0 s | 37.7 s |  |
| rescale search, unmarked (nothing to find) | 752×600 | 3 | 13.6 s | 14.3 s | 14.3 s | 30.2 s |  |
| rescale search, unmarked (nothing to find) | 1282×1110 | 3 | 13.9 s | 19.8 s | 20.5 s | 9.7 s | 1 |
