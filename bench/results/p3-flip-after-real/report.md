# Watermark benchmark — `standard` suite
_2026-09-21T20:34:57+00:00 · 1197 trials in 128.4 s · seed 20260919_

wmcore fingerprint `43bd87e6dee4` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: real images from `/home/claude/real`.

## Headline

- **`ss` detection** over gated attacks: 41/42 = 97.6% [87.7%-99.6%]; weakest gated attack `jpeg_75` at 0.0% (n=1).
- **`ss_id` detection** over gated attacks: 14/14 = 100.0% [78.5%-100.0%]; weakest gated attack `identity` at 100.0% (n=1).
- **`ss_flip` detection** over gated attacks: 69/70 = 98.6% [92.3%-99.7%]; weakest gated attack `jpeg_75` at 0.0% (n=1).
- **`ss_id_flip` detection** over gated attacks: 42/42 = 100.0% [91.6%-100.0%]; weakest gated attack `flip_both` at 100.0% (n=1).
- **`ss` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss_id` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss_flip` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss_id_flip` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss` wrong-key acceptance**: 37/168 = 22.0% (95% upper bound 29.1%); exact payload recovered in 35/168.
- **`ss_id` wrong-key acceptance**: 41/168 = 24.4% (95% upper bound 31.6%); exact payload recovered in 41/168.
- **`ss_flip` wrong-key acceptance**: 43/168 = 25.6% (95% upper bound 32.9%); exact payload recovered in 41/168.
- **`ss_id_flip` wrong-key acceptance**: 41/168 = 24.4% (95% upper bound 31.6%); exact payload recovered in 41/168.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · file 1282×1110 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 177 ms | 177 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 207 ms | 207 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 175 ms | 175 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 185 ms | 185 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.022 | 0.000 | 174 ms | 174 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 179 ms | 179 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 176 ms | 176 ms |  |

#### `ss` · file 1282×1110 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 176 ms | 176 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 172 ms | 172 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 174 ms | 174 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 174 ms | 174 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.019 | 0.000 | 174 ms | 174 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 178 ms | 178 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 171 ms | 171 ms |  |

#### `ss` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 172 ms | 172 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 172 ms | 172 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 171 ms | 171 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 178 ms | 178 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.023 | 0.000 | 174 ms | 174 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 175 ms | 175 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 176 ms | 176 ms |  |

#### `ss` · file 493×356 · α=12 · payload `medium` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 21 ms | 21 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.058 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.070 | 0.015 | 20 ms | 20 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.054 | 0.000 | 20 ms | 20 ms |  |
| jpeg_75 | 1 | 0.0% [0%–79%] | 100.0% | 0.058 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |

#### `ss` · file 493×356 · α=12 · payload `short` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 21 ms | 21 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.060 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 20 ms | 20 ms |  |

#### `ss` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 19 ms | 19 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 19 ms | 19 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.066 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 20 ms | 20 ms |  |

#### `ss` · file 512×480 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 28 ms | 28 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 30 ms |  |

#### `ss` · file 512×480 · α=12 · payload `short` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.013 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 28 ms | 28 ms |  |

#### `ss` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 28 ms | 28 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.008 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 28 ms | 28 ms |  |

#### `ss` · file 512×512 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 32 ms | 32 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.027 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.034 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 31 ms | 31 ms |  |

#### `ss` · file 512×512 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 30 ms | 31 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.028 | 0.000 | 31 ms | 32 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 31 ms | 32 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.032 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 32 ms | 32 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.028 | 0.000 | 30 ms | 31 ms |  |

#### `ss` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.025 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.027 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.030 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 30 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 32 ms | 32 ms |  |

#### `ss` · file 640×480 · α=12 · payload `medium` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.116 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.116 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 35 ms | 35 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms |  |

#### `ss` · file 640×480 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.127 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.141 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 34 ms | 34 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.128 | 0.000 | 35 ms | 35 ms |  |

#### `ss` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.115 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.115 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.127 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 34 ms | 34 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms |  |

#### `ss` · file 752×600 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.036 | 0.000 | 52 ms | 52 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 53 ms | 53 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.037 | 0.000 | 53 ms | 53 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.036 | 0.000 | 56 ms | 56 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.046 | 0.000 | 53 ms | 53 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.036 | 0.000 | 55 ms | 55 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.037 | 0.000 | 52 ms | 52 ms |  |

#### `ss` · file 752×600 · α=12 · payload `short` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 51 ms | 51 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 57 ms | 57 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 53 ms | 53 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 54 ms | 54 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.057 | 0.000 | 52 ms | 52 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 54 ms | 54 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 52 ms | 52 ms |  |

#### `ss` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.039 | 0.000 | 51 ms | 51 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 51 ms | 51 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.044 | 0.000 | 48 ms | 48 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.039 | 0.000 | 50 ms | 50 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.061 | 0.000 | 51 ms | 51 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 52 ms | 52 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 51 ms | 51 ms |  |

#### `ss_flip` · file 1282×1110 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 583 ms | 583 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 599 ms | 599 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 583 ms | 583 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 590 ms | 590 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.022 | 0.000 | 583 ms | 583 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 587 ms | 587 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 621 ms | 621 ms |  |

#### `ss_flip` · file 1282×1110 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 603 ms | 603 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 582 ms | 582 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 582 ms | 582 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 568 ms | 568 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.019 | 0.000 | 584 ms | 584 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 579 ms | 579 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 578 ms | 578 ms |  |

#### `ss_flip` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 574 ms | 574 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 312 ms | 312 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 312 ms | 312 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 459 ms | 459 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.023 | 0.000 | 440 ms | 440 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 177 ms | 177 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 176 ms | 176 ms |  |

#### `ss_flip` · file 493×356 · α=12 · payload `medium` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 73 ms | 73 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 72 ms | 72 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.058 | 0.000 | 73 ms | 73 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 74 ms | 74 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.070 | 0.015 | 72 ms | 72 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.054 | 0.000 | 73 ms | 73 ms |  |
| jpeg_75 | 1 | 0.0% [0%–79%] | 100.0% | 0.058 | 0.000 | 72 ms | 72 ms | signal intact - decoder loses sync |

#### `ss_flip` · file 493×356 · α=12 · payload `short` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 73 ms | 73 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 74 ms | 74 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 74 ms | 74 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 73 ms | 73 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.060 | 0.000 | 73 ms | 73 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 72 ms | 72 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 72 ms | 72 ms |  |

#### `ss_flip` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 70 ms | 70 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 37 ms | 37 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.053 | 0.000 | 38 ms | 38 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 54 ms | 54 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.066 | 0.000 | 54 ms | 54 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 20 ms | 20 ms |  |

#### `ss_flip` · file 512×480 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 101 ms | 101 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 101 ms | 101 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 101 ms | 101 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 101 ms | 101 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 103 ms | 103 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 106 ms | 106 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 103 ms | 103 ms |  |

#### `ss_flip` · file 512×480 · α=12 · payload `short` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 102 ms | 102 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 102 ms | 102 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 101 ms | 101 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 102 ms | 102 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.013 | 0.000 | 101 ms | 101 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 102 ms | 102 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 102 ms | 102 ms |  |

#### `ss_flip` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 103 ms | 103 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 52 ms | 52 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 56 ms | 56 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 77 ms | 77 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.008 | 0.000 | 76 ms | 76 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 28 ms | 28 ms |  |

#### `ss_flip` · file 512×512 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 108 ms | 109 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 111 ms | 111 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.027 | 0.000 | 108 ms | 109 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 111 ms | 113 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.034 | 0.000 | 107 ms | 108 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 110 ms | 110 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 110 ms | 111 ms |  |

#### `ss_flip` · file 512×512 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 109 ms | 110 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 109 ms | 112 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.028 | 0.000 | 109 ms | 111 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 109 ms | 111 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.032 | 0.000 | 110 ms | 110 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 111 ms | 112 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.028 | 0.000 | 109 ms | 111 ms |  |

#### `ss_flip` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 108 ms | 109 ms |  |
| †flip_horizontal | 2 | 100.0% [34%–100%] | 0.0% | n/a | n/a | 57 ms | 57 ms |  |
| flip_horizontal_jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 57 ms | 57 ms |  |
| flip_vertical | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 82 ms | 83 ms |  |
| flip_vertical_jpeg_50 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 82 ms | 84 ms |  |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 31 ms | 32 ms |  |

#### `ss_flip` · file 640×480 · α=12 · payload `medium` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.116 | 0.000 | 126 ms | 126 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 125 ms | 125 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 125 ms | 125 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.116 | 0.000 | 125 ms | 125 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 123 ms | 123 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 126 ms | 126 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 131 ms | 131 ms |  |

#### `ss_flip` · file 640×480 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 122 ms | 122 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 123 ms | 123 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.127 | 0.000 | 122 ms | 122 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 123 ms | 123 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.141 | 0.000 | 123 ms | 123 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 122 ms | 122 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.128 | 0.000 | 123 ms | 123 ms |  |

#### `ss_flip` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 123 ms | 123 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 63 ms | 63 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 63 ms | 63 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 91 ms | 91 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.127 | 0.000 | 93 ms | 93 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 35 ms | 35 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms |  |

#### `ss_flip` · file 752×600 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.036 | 0.000 | 191 ms | 191 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 188 ms | 188 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.037 | 0.000 | 186 ms | 186 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.036 | 0.000 | 189 ms | 189 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.046 | 0.000 | 180 ms | 180 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.036 | 0.000 | 187 ms | 187 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.037 | 0.000 | 182 ms | 182 ms |  |

#### `ss_flip` · file 752×600 · α=12 · payload `short` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 184 ms | 184 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 184 ms | 184 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 183 ms | 183 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 185 ms | 185 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.057 | 0.000 | 182 ms | 182 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 189 ms | 189 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 186 ms | 186 ms |  |

#### `ss_flip` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 179 ms | 179 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 94 ms | 94 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 93 ms | 93 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 138 ms | 138 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.061 | 0.000 | 146 ms | 146 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 52 ms | 52 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 51 ms | 51 ms |  |

#### `ss_id` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 168 ms | 168 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 183 ms | 183 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 174 ms | 174 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 182 ms | 182 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.023 | 0.000 | 173 ms | 173 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 174 ms | 174 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 175 ms | 175 ms |  |

#### `ss_id` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.066 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 20 ms | 20 ms |  |

#### `ss_id` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 28 ms | 28 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.008 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 28 ms | 28 ms |  |

#### `ss_id` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.025 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.027 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.030 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 32 ms | 33 ms |  |

#### `ss_id` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.115 | 0.000 | 34 ms | 34 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.115 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.127 | 0.000 | 36 ms | 36 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 35 ms | 35 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms |  |

#### `ss_id` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.039 | 0.000 | 52 ms | 52 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 51 ms | 51 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.044 | 0.000 | 51 ms | 51 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.039 | 0.000 | 51 ms | 51 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.061 | 0.000 | 51 ms | 51 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 52 ms | 52 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 51 ms | 51 ms |  |

#### `ss_id_flip` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 573 ms | 573 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 310 ms | 310 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 309 ms | 309 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 442 ms | 442 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.023 | 0.000 | 449 ms | 449 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 177 ms | 177 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 175 ms | 175 ms |  |

#### `ss_id_flip` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 71 ms | 71 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 37 ms | 37 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.053 | 0.000 | 38 ms | 38 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 54 ms | 54 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.066 | 0.000 | 55 ms | 55 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 20 ms | 20 ms |  |

#### `ss_id_flip` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 103 ms | 103 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 53 ms | 53 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 54 ms | 54 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 80 ms | 80 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.008 | 0.000 | 77 ms | 77 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 28 ms | 28 ms |  |

#### `ss_id_flip` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 108 ms | 108 ms |  |
| †flip_horizontal | 2 | 100.0% [34%–100%] | 0.0% | n/a | n/a | 58 ms | 58 ms |  |
| flip_horizontal_jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 57 ms | 57 ms |  |
| flip_vertical | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 83 ms | 84 ms |  |
| flip_vertical_jpeg_50 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 84 ms | 85 ms |  |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 31 ms | 31 ms |  |

#### `ss_id_flip` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 126 ms | 126 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 64 ms | 64 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 65 ms | 65 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 92 ms | 92 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.127 | 0.000 | 93 ms | 93 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 35 ms | 35 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms |  |

#### `ss_id_flip` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 179 ms | 179 ms |  |
| †flip_horizontal | 1 | 100.0% [21%–100%] | 0.0% | n/a | n/a | 95 ms | 95 ms |  |
| flip_horizontal_jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 94 ms | 94 ms |  |
| flip_vertical | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 138 ms | 138 ms |  |
| flip_vertical_jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.061 | 0.000 | 139 ms | 139 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 51 ms | 51 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 51 ms | 51 ms |  |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
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
| unmarked image | ss_flip | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | identity | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | identity | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | identity | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_flip | identity | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | identity | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | jpeg_75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | jpeg_75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | jpeg_75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | jpeg_75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_flip | jpeg_75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | jpeg_75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_0.75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_0.75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_0.75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_0.75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_flip | resize_0.75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_0.75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_1.25 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_1.25 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_1.25 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_1.25 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_flip | resize_1.25 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_flip | resize_1.25 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | identity | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | identity | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | identity | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id | identity | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | identity | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | jpeg_75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | jpeg_75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | jpeg_75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | jpeg_75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id | jpeg_75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | jpeg_75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_0.75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_0.75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_0.75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_0.75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id | resize_0.75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_0.75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_1.25 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_1.25 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_1.25 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_1.25 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id | resize_1.25 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id | resize_1.25 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | identity | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | identity | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | identity | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | identity | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id_flip | identity | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | identity | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | jpeg_75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | jpeg_75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | jpeg_75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | jpeg_75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id_flip | jpeg_75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | jpeg_75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_0.75 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_0.75 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_0.75 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_0.75 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id_flip | resize_0.75 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_0.75 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_1.25 | file 1282×1110 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_1.25 | file 493×356 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_1.25 | file 512×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_1.25 | file 512×512 | 2 | 0 | 0.0% (≤84.2%) | — |
| unmarked image | ss_id_flip | resize_1.25 | file 640×480 | 1 | 0 | 0.0% (≤97.5%) | — |
| unmarked image | ss_id_flip | resize_1.25 | file 752×600 | 1 | 0 | 0.0% (≤97.5%) | — |
| marked, wrong key | ss | identity | file 1282×1110 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss | identity | file 493×356 | 12 | 1 | 8.3% (≤38.5%) | 1 |
| marked, wrong key | ss | identity | file 512×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss | identity | file 512×512 | 24 | 6 | 25.0% (≤46.7%) | 6 |
| marked, wrong key | ss | identity | file 640×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss | identity | file 752×600 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss | jpeg_75 | file 1282×1110 | 12 | 4 | 33.3% (≤65.1%) | 4 |
| marked, wrong key | ss | jpeg_75 | file 493×356 | 12 | 2 | 16.7% (≤48.4%) | 0 |
| marked, wrong key | ss | jpeg_75 | file 512×480 | 12 | 0 | 0.0% (≤26.5%) | 0 |
| marked, wrong key | ss | jpeg_75 | file 512×512 | 24 | 4 | 16.7% (≤37.4%) | 4 |
| marked, wrong key | ss | jpeg_75 | file 640×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss | jpeg_75 | file 752×600 | 12 | 4 | 33.3% (≤65.1%) | 4 |
| marked, wrong key | ss_flip | identity | file 1282×1110 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss_flip | identity | file 493×356 | 12 | 1 | 8.3% (≤38.5%) | 1 |
| marked, wrong key | ss_flip | identity | file 512×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_flip | identity | file 512×512 | 24 | 6 | 25.0% (≤46.7%) | 6 |
| marked, wrong key | ss_flip | identity | file 640×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_flip | identity | file 752×600 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss_flip | jpeg_75 | file 1282×1110 | 12 | 6 | 50.0% (≤78.9%) | 6 |
| marked, wrong key | ss_flip | jpeg_75 | file 493×356 | 12 | 2 | 16.7% (≤48.4%) | 0 |
| marked, wrong key | ss_flip | jpeg_75 | file 512×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_flip | jpeg_75 | file 512×512 | 24 | 5 | 20.8% (≤42.2%) | 5 |
| marked, wrong key | ss_flip | jpeg_75 | file 640×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_flip | jpeg_75 | file 752×600 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss_id | identity | file 1282×1110 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss_id | identity | file 493×356 | 12 | 1 | 8.3% (≤38.5%) | 1 |
| marked, wrong key | ss_id | identity | file 512×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_id | identity | file 512×512 | 24 | 6 | 25.0% (≤46.7%) | 6 |
| marked, wrong key | ss_id | identity | file 640×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_id | identity | file 752×600 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss_id | jpeg_75 | file 1282×1110 | 12 | 6 | 50.0% (≤78.9%) | 6 |
| marked, wrong key | ss_id | jpeg_75 | file 493×356 | 12 | 0 | 0.0% (≤26.5%) | 0 |
| marked, wrong key | ss_id | jpeg_75 | file 512×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_id | jpeg_75 | file 512×512 | 24 | 5 | 20.8% (≤42.2%) | 5 |
| marked, wrong key | ss_id | jpeg_75 | file 640×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_id | jpeg_75 | file 752×600 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss_id_flip | identity | file 1282×1110 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss_id_flip | identity | file 493×356 | 12 | 1 | 8.3% (≤38.5%) | 1 |
| marked, wrong key | ss_id_flip | identity | file 512×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_id_flip | identity | file 512×512 | 24 | 6 | 25.0% (≤46.7%) | 6 |
| marked, wrong key | ss_id_flip | identity | file 640×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_id_flip | identity | file 752×600 | 12 | 5 | 41.7% (≤72.3%) | 5 |
| marked, wrong key | ss_id_flip | jpeg_75 | file 1282×1110 | 12 | 6 | 50.0% (≤78.9%) | 6 |
| marked, wrong key | ss_id_flip | jpeg_75 | file 493×356 | 12 | 0 | 0.0% (≤26.5%) | 0 |
| marked, wrong key | ss_id_flip | jpeg_75 | file 512×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_id_flip | jpeg_75 | file 512×512 | 24 | 5 | 20.8% (≤42.2%) | 5 |
| marked, wrong key | ss_id_flip | jpeg_75 | file 640×480 | 12 | 2 | 16.7% (≤48.4%) | 2 |
| marked, wrong key | ss_id_flip | jpeg_75 | file 752×600 | 12 | 5 | 41.7% (≤72.3%) | 5 |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss | 493×356 | 3 | 20 ms | 20 ms | 20 ms | 114 ms |  |
| decode:ss | 512×480 | 3 | 29 ms | 29 ms | 29 ms | 117 ms |  |
| decode:ss | 512×512 | 6 | 31 ms | 32 ms | 32 ms | 118 ms |  |
| decode:ss | 640×480 | 3 | 34 ms | 35 ms | 35 ms | 112 ms |  |
| decode:ss | 752×600 | 3 | 54 ms | 55 ms | 55 ms | 119 ms |  |
| decode:ss | 1282×1110 | 3 | 178 ms | 179 ms | 179 ms | 125 ms |  |
| decode:ss_flip | 493×356 | 3 | 72 ms | 73 ms | 73 ms | 413 ms |  |
| decode:ss_flip | 512×480 | 3 | 102 ms | 105 ms | 106 ms | 415 ms |  |
| decode:ss_flip | 512×512 | 6 | 110 ms | 112 ms | 112 ms | 419 ms |  |
| decode:ss_flip | 640×480 | 3 | 122 ms | 125 ms | 126 ms | 397 ms |  |
| decode:ss_flip | 752×600 | 3 | 187 ms | 189 ms | 189 ms | 415 ms |  |
| decode:ss_flip | 1282×1110 | 3 | 579 ms | 586 ms | 587 ms | 407 ms |  |
| decode:ss_id | 493×356 | 1 | 20 ms | 20 ms | 20 ms | 114 ms |  |
| decode:ss_id | 512×480 | 1 | 30 ms | 30 ms | 30 ms | 121 ms |  |
| decode:ss_id | 512×512 | 2 | 31 ms | 31 ms | 31 ms | 119 ms |  |
| decode:ss_id | 640×480 | 1 | 35 ms | 35 ms | 35 ms | 114 ms |  |
| decode:ss_id | 752×600 | 1 | 52 ms | 52 ms | 52 ms | 115 ms |  |
| decode:ss_id | 1282×1110 | 1 | 174 ms | 174 ms | 174 ms | 122 ms |  |
| decode:ss_id_flip | 493×356 | 1 | 20 ms | 20 ms | 20 ms | 114 ms |  |
| decode:ss_id_flip | 512×480 | 1 | 29 ms | 29 ms | 29 ms | 116 ms |  |
| decode:ss_id_flip | 512×512 | 2 | 31 ms | 31 ms | 31 ms | 118 ms |  |
| decode:ss_id_flip | 640×480 | 1 | 35 ms | 35 ms | 35 ms | 113 ms |  |
| decode:ss_id_flip | 752×600 | 1 | 51 ms | 51 ms | 51 ms | 113 ms |  |
| decode:ss_id_flip | 1282×1110 | 1 | 177 ms | 177 ms | 177 ms | 124 ms |  |
| embed:ss | 493×356 | 3 | 35 ms | 36 ms | 36 ms | 202 ms |  |
| embed:ss | 512×480 | 3 | 51 ms | 52 ms | 53 ms | 207 ms |  |
| embed:ss | 512×512 | 6 | 58 ms | 60 ms | 60 ms | 220 ms |  |
| embed:ss | 640×480 | 3 | 67 ms | 69 ms | 69 ms | 219 ms |  |
| embed:ss | 752×600 | 3 | 101 ms | 103 ms | 103 ms | 224 ms |  |
| embed:ss | 1282×1110 | 3 | 447 ms | 467 ms | 469 ms | 314 ms |  |
