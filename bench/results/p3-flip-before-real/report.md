# Watermark benchmark — `standard` suite
_2026-09-21T19:52:22+00:00 · 609 trials in 45.1 s · seed 20260919_

wmcore fingerprint `b4df979c2348` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: real images from `/home/claude/real`.

## Headline

- **`ss` detection** over gated attacks: 41/42 = 97.6% [87.7%-99.6%]; weakest gated attack `jpeg_75` at 0.0% (n=1).
- **`ss_id` detection** over gated attacks: 14/14 = 100.0% [78.5%-100.0%]; weakest gated attack `identity` at 100.0% (n=1).
- **`ss` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss_id` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss` wrong-key acceptance**: 37/168 = 22.0% (95% upper bound 29.1%); exact payload recovered in 35/168.
- **`ss_id` wrong-key acceptance**: 41/168 = 24.4% (95% upper bound 31.6%); exact payload recovered in 41/168.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · file 1282×1110 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 184 ms | 184 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 183 ms | 183 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 188 ms | 188 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 179 ms | 179 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.022 | 0.000 | 181 ms | 181 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 182 ms | 182 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 184 ms | 184 ms |  |

#### `ss` · file 1282×1110 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 179 ms | 179 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 184 ms | 184 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 188 ms | 188 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 181 ms | 181 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.019 | 0.000 | 176 ms | 176 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 182 ms | 182 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 192 ms | 192 ms |  |

#### `ss` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 186 ms | 186 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 191 ms | 191 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 179 ms | 179 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 183 ms | 183 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.023 | 0.000 | 182 ms | 182 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 187 ms | 187 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 181 ms | 181 ms |  |

#### `ss` · file 493×356 · α=12 · payload `medium` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 21 ms | 21 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.058 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 22 ms | 22 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.070 | 0.015 | 20 ms | 20 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.054 | 0.000 | 21 ms | 21 ms |  |
| jpeg_75 | 1 | 0.0% [0%–79%] | 100.0% | 0.058 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |

#### `ss` · file 493×356 · α=12 · payload `short` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.060 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 20 ms | 20 ms |  |

#### `ss` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.066 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 21 ms | 21 ms |  |

#### `ss` · file 512×480 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 28 ms | 28 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 28 ms | 28 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 28 ms | 28 ms |  |

#### `ss` · file 512×480 · α=12 · payload `short` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 28 ms | 28 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.013 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 30 ms | 30 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.007 | 0.000 | 29 ms | 29 ms |  |

#### `ss` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 28 ms | 28 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.008 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 28 ms | 28 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 28 ms | 28 ms |  |

#### `ss` · file 512×512 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 30 ms | 31 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.027 | 0.000 | 30 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.034 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 32 ms | 33 ms |  |

#### `ss` · file 512×512 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 32 ms | 33 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.028 | 0.000 | 32 ms | 32 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.026 | 0.000 | 31 ms | 32 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.032 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.028 | 0.000 | 31 ms | 32 ms |  |

#### `ss` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 33 ms | 34 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.027 | 0.000 | 31 ms | 32 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.030 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 33 ms | 34 ms |  |

#### `ss` · file 640×480 · α=12 · payload `medium` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.116 | 0.000 | 37 ms | 37 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 36 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.116 | 0.000 | 36 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 37 ms | 37 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 35 ms | 35 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 36 ms | 36 ms |  |

#### `ss` · file 640×480 · α=12 · payload `short` · PSNR 32.5 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 36 ms | 36 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 39 ms | 39 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.127 | 0.000 | 36 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 37 ms | 37 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.141 | 0.000 | 36 ms | 36 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 36 ms | 36 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.128 | 0.000 | 38 ms | 38 ms |  |

#### `ss` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.115 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 41 ms | 41 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.127 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms |  |

#### `ss` · file 752×600 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.036 | 0.000 | 61 ms | 61 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 59 ms | 59 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.037 | 0.000 | 54 ms | 54 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.036 | 0.000 | 59 ms | 59 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.046 | 0.000 | 59 ms | 59 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.036 | 0.000 | 62 ms | 62 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.037 | 0.000 | 61 ms | 61 ms |  |

#### `ss` · file 752×600 · α=12 · payload `short` · PSNR 32.8 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 58 ms | 58 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 58 ms | 58 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 56 ms | 56 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.040 | 0.000 | 57 ms | 57 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.057 | 0.000 | 75 ms | 75 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 66 ms | 66 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 58 ms | 58 ms |  |

#### `ss` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.039 | 0.000 | 60 ms | 60 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 60 ms | 60 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.044 | 0.000 | 55 ms | 55 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.039 | 0.000 | 62 ms | 62 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.061 | 0.000 | 60 ms | 60 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 61 ms | 61 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 61 ms | 61 ms |  |

#### `ss_id` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 184 ms | 184 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 193 ms | 193 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 183 ms | 183 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 206 ms | 206 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.023 | 0.000 | 179 ms | 179 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 186 ms | 186 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 179 ms | 179 ms |  |

#### `ss_id` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.066 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 21 ms | 21 ms |  |

#### `ss_id` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.008 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 28 ms | 28 ms |  |

#### `ss_id` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 2 | 0.0% [0%–66%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 32 ms | 32 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 2 | 0.0% [0%–66%] | 0.0% | 0.027 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical | 2 | 0.0% [0%–66%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 2 | 0.0% [0%–66%] | 0.0% | 0.030 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 34 ms | 35 ms |  |

#### `ss_id` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.115 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 38 ms | 38 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.127 | 0.000 | 37 ms | 37 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 35 ms | 35 ms |  |

#### `ss_id` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 1 | 0.0% [0%–79%] | 0.0% | 0.039 | 0.000 | 60 ms | 60 ms | signal intact - decoder loses sync |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 62 ms | 62 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 1 | 0.0% [0%–79%] | 0.0% | 0.044 | 0.000 | 80 ms | 80 ms | signal intact - decoder loses sync |
| †flip_vertical | 1 | 0.0% [0%–79%] | 0.0% | 0.039 | 0.000 | 61 ms | 61 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 1 | 0.0% [0%–79%] | 0.0% | 0.061 | 0.000 | 59 ms | 59 ms | signal intact - decoder loses sync |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 61 ms | 61 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 60 ms | 60 ms |  |

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

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss | 493×356 | 3 | 21 ms | 21 ms | 21 ms | 119 ms |  |
| decode:ss | 512×480 | 3 | 28 ms | 30 ms | 30 ms | 114 ms |  |
| decode:ss | 512×512 | 6 | 31 ms | 31 ms | 31 ms | 117 ms |  |
| decode:ss | 640×480 | 3 | 36 ms | 36 ms | 36 ms | 116 ms |  |
| decode:ss | 752×600 | 3 | 62 ms | 66 ms | 66 ms | 137 ms |  |
| decode:ss | 1282×1110 | 3 | 182 ms | 187 ms | 187 ms | 128 ms |  |
| decode:ss_id | 493×356 | 1 | 20 ms | 20 ms | 20 ms | 116 ms |  |
| decode:ss_id | 512×480 | 1 | 29 ms | 29 ms | 29 ms | 117 ms |  |
| decode:ss_id | 512×512 | 2 | 31 ms | 31 ms | 31 ms | 119 ms |  |
| decode:ss_id | 640×480 | 1 | 36 ms | 36 ms | 36 ms | 117 ms |  |
| decode:ss_id | 752×600 | 1 | 61 ms | 61 ms | 61 ms | 134 ms |  |
| decode:ss_id | 1282×1110 | 1 | 186 ms | 186 ms | 186 ms | 130 ms |  |
| embed:ss | 493×356 | 3 | 38 ms | 38 ms | 38 ms | 218 ms |  |
| embed:ss | 512×480 | 3 | 55 ms | 58 ms | 59 ms | 225 ms |  |
| embed:ss | 512×512 | 6 | 59 ms | 68 ms | 70 ms | 225 ms |  |
| embed:ss | 640×480 | 3 | 70 ms | 77 ms | 78 ms | 228 ms |  |
| embed:ss | 752×600 | 3 | 109 ms | 122 ms | 123 ms | 242 ms |  |
| embed:ss | 1282×1110 | 3 | 467 ms | 489 ms | 491 ms | 329 ms |  |
