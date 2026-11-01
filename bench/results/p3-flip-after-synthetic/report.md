# Watermark benchmark — `standard` suite
_2026-09-21T20:32:42+00:00 · 5968 trials in 29.5 s · seed 20260919_

wmcore fingerprint `43bd87e6dee4` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss` detection** over gated attacks: 288/288 = 100.0% [98.7%-100.0%]; weakest gated attack `identity` at 100.0% (n=12).
- **`ss_id` detection** over gated attacks: 96/96 = 100.0% [96.2%-100.0%]; weakest gated attack `identity` at 100.0% (n=12).
- **`ss_flip` detection** over gated attacks: 480/480 = 100.0% [99.2%-100.0%]; weakest gated attack `flip_both` at 100.0% (n=12).
- **`ss_id_flip` detection** over gated attacks: 288/288 = 100.0% [98.7%-100.0%]; weakest gated attack `flip_both` at 100.0% (n=12).
- **`ss` unmarked-image FPR**: 0/400 = 0.0% (95% upper bound 0.9%).
- **`ss_id` unmarked-image FPR**: 0/400 = 0.0% (95% upper bound 0.9%).
- **`ss_flip` unmarked-image FPR**: 0/400 = 0.0% (95% upper bound 0.9%).
- **`ss_id_flip` unmarked-image FPR**: 0/400 = 0.0% (95% upper bound 0.9%).
- **`ss` wrong-key acceptance**: 65/384 = 16.9% (95% upper bound 21.1%); exact payload recovered in 64/384.
- **`ss_id` wrong-key acceptance**: 112/384 = 29.2% (95% upper bound 34.0%); exact payload recovered in 112/384.
- **`ss_flip` wrong-key acceptance**: 113/384 = 29.4% (95% upper bound 34.3%); exact payload recovered in 112/384.
- **`ss_id_flip` wrong-key acceptance**: 112/384 = 29.2% (95% upper bound 34.0%); exact payload recovered in 112/384.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · gradnoise 320×240 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |

#### `ss` · gradnoise 320×240 · α=12 · payload `short` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 16.7% | 0.000 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |

#### `ss` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 8.3% | 0.000 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 12 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |

#### `ss` · gradnoise 640×480 · α=12 · payload `medium` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 40 ms | 41 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 37 ms | 38 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 39 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 40 ms | 41 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 41 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms |  |

#### `ss` · gradnoise 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 8.3% | 0.000 | 0.000 | 39 ms | 41 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 8.3% | n/a | n/a | 40 ms | 41 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 37 ms | 41 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 41 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |

#### `ss` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 8.3% | n/a | n/a | 39 ms | 40 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 37 ms | 38 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 41 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 41 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |

#### `ss` · pink 320×240 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.005 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.008 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |

#### `ss` · pink 320×240 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 11 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 9 ms | 11 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.008 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 10 ms |  |

#### `ss` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 9 ms | 11 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.005 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.007 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 10 ms |  |

#### `ss` · pink 640×480 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 40 ms | 43 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 38 ms | 39 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 40 ms | 41 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 40 ms | 50 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 39 ms | 41 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 39 ms | 41 ms |  |

#### `ss` · pink 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 40 ms | 44 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 38 ms | 41 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 8.3% | 0.004 | 0.000 | 40 ms | 43 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 39 ms | 44 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 40 ms | 42 ms |  |

#### `ss` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 8.3% | 0.003 | 0.000 | 39 ms | 51 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 39 ms | 59 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 38 ms | 40 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 40 ms | 58 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 40 ms | 42 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 39 ms | 58 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 39 ms | 59 ms |  |

#### `ss_flip` · gradnoise 320×240 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 35 ms | 36 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 35 ms | 35 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 35 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 35 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 35 ms | 37 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 35 ms | 35 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 35 ms | 35 ms |  |

#### `ss_flip` · gradnoise 320×240 · α=12 · payload `short` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 35 ms | 42 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 34 ms | 37 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 35 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 16.7% | 0.000 | 0.000 | 35 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 34 ms | 37 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 34 ms | 36 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 35 ms | 37 ms |  |

#### `ss_flip` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 34 ms | 35 ms |  |
| †flip_horizontal | 12 | 100.0% [76%–100%] | 0.0% | n/a | n/a | 18 ms | 18 ms |  |
| flip_horizontal_jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 18 ms | 18 ms |  |
| flip_vertical | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 26 ms | 28 ms |  |
| flip_vertical_jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 26 ms | 27 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |

#### `ss_flip` · gradnoise 640×480 · α=12 · payload `medium` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 127 ms | 132 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 128 ms | 129 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 127 ms | 129 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 127 ms | 130 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 128 ms | 132 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 128 ms | 130 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 128 ms | 131 ms |  |

#### `ss_flip` · gradnoise 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 8.3% | 0.000 | 0.000 | 128 ms | 135 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 8.3% | n/a | n/a | 127 ms | 136 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 128 ms | 134 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 128 ms | 133 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 127 ms | 130 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 127 ms | 131 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 127 ms | 136 ms |  |

#### `ss_flip` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 127 ms | 129 ms |  |
| †flip_horizontal | 12 | 100.0% [76%–100%] | 0.0% | n/a | n/a | 69 ms | 71 ms |  |
| flip_horizontal_jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 69 ms | 70 ms |  |
| flip_vertical | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 99 ms | 105 ms |  |
| flip_vertical_jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 98 ms | 100 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 40 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms |  |

#### `ss_flip` · pink 320×240 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 35 ms | 36 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 34 ms | 35 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.005 | 0.000 | 35 ms | 39 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 34 ms | 35 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.008 | 0.000 | 34 ms | 36 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 34 ms | 35 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 34 ms | 37 ms |  |

#### `ss_flip` · pink 320×240 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 34 ms | 36 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 35 ms | 43 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 34 ms | 36 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 34 ms | 43 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.008 | 0.000 | 34 ms | 38 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 34 ms | 35 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 34 ms | 36 ms |  |

#### `ss_flip` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 34 ms | 35 ms |  |
| †flip_horizontal | 12 | 100.0% [76%–100%] | 0.0% | n/a | n/a | 18 ms | 22 ms |  |
| flip_horizontal_jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 18 ms | 18 ms |  |
| flip_vertical | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 26 ms | 32 ms |  |
| flip_vertical_jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.007 | 0.000 | 26 ms | 27 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 10 ms |  |

#### `ss_flip` · pink 640×480 · α=12 · payload `medium` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 129 ms | 133 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 129 ms | 140 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 128 ms | 152 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 128 ms | 133 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 128 ms | 133 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 128 ms | 132 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 128 ms | 133 ms |  |

#### `ss_flip` · pink 640×480 · α=12 · payload `short` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 129 ms | 133 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 130 ms | 132 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 128 ms | 138 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 8.3% | 0.004 | 0.000 | 130 ms | 140 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 129 ms | 131 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 128 ms | 133 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 129 ms | 133 ms |  |

#### `ss_flip` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 128 ms | 131 ms |  |
| †flip_horizontal | 12 | 100.0% [76%–100%] | 0.0% | n/a | n/a | 70 ms | 109 ms |  |
| flip_horizontal_jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 69 ms | 73 ms |  |
| flip_vertical | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 99 ms | 102 ms |  |
| flip_vertical_jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.006 | 0.000 | 99 ms | 126 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 40 ms | 60 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 40 ms | 59 ms |  |

#### `ss_id` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 10 ms | 12 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |

#### `ss_id` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 39 ms | 40 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 38 ms | 39 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 42 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms |  |

#### `ss_id` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 10 ms | 10 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 10 ms | 12 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.005 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 10 ms | 11 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.007 | 0.000 | 9 ms | 10 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 10 ms |  |

#### `ss_id` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| †flip_both | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 39 ms | 42 ms | signal intact - decoder loses sync |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 40 ms | 60 ms | no oracle geometry |
| †flip_horizontal_jpeg_75 | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 38 ms | 40 ms | signal intact - decoder loses sync |
| †flip_vertical | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 39 ms | 49 ms | signal intact - decoder loses sync |
| †flip_vertical_jpeg_50 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 39 ms | 41 ms | signal intact - decoder loses sync |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 39 ms | 59 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 40 ms | 60 ms |  |

#### `ss_id_flip` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 34 ms | 35 ms |  |
| †flip_horizontal | 12 | 100.0% [76%–100%] | 0.0% | n/a | n/a | 18 ms | 21 ms |  |
| flip_horizontal_jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 18 ms | 19 ms |  |
| flip_vertical | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 26 ms | 27 ms |  |
| flip_vertical_jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 26 ms | 26 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |

#### `ss_id_flip` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 128 ms | 129 ms |  |
| †flip_horizontal | 12 | 100.0% [76%–100%] | 0.0% | n/a | n/a | 70 ms | 71 ms |  |
| flip_horizontal_jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 70 ms | 71 ms |  |
| flip_vertical | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 99 ms | 101 ms |  |
| flip_vertical_jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 100 ms | 100 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 38 ms | 39 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 39 ms | 40 ms |  |

#### `ss_id_flip` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 34 ms | 35 ms |  |
| †flip_horizontal | 12 | 100.0% [76%–100%] | 0.0% | n/a | n/a | 18 ms | 23 ms |  |
| flip_horizontal_jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 18 ms | 18 ms |  |
| flip_vertical | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 26 ms | 27 ms |  |
| flip_vertical_jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.007 | 0.000 | 26 ms | 27 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 11 ms |  |

#### `ss_id_flip` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| flip_both | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 129 ms | 138 ms |  |
| †flip_horizontal | 12 | 100.0% [76%–100%] | 0.0% | n/a | n/a | 70 ms | 111 ms |  |
| flip_horizontal_jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 70 ms | 73 ms |  |
| flip_vertical | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 100 ms | 120 ms |  |
| flip_vertical_jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.006 | 0.000 | 99 ms | 103 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 40 ms | 59 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 40 ms | 59 ms |  |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss | identity | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | identity | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | identity | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | identity | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | jpeg_75 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | jpeg_75 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | jpeg_75 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | jpeg_75 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | resize_0.75 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | resize_0.75 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | resize_0.75 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | resize_0.75 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | resize_1.25 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | resize_1.25 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | resize_1.25 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss | resize_1.25 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | identity | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | identity | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | identity | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | identity | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | jpeg_75 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | jpeg_75 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | jpeg_75 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | jpeg_75 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | resize_0.75 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | resize_0.75 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | resize_0.75 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | resize_0.75 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | resize_1.25 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | resize_1.25 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | resize_1.25 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_flip | resize_1.25 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | identity | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | identity | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | identity | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | identity | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | jpeg_75 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | jpeg_75 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | jpeg_75 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | jpeg_75 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | resize_0.75 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | resize_0.75 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | resize_0.75 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | resize_0.75 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | resize_1.25 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | resize_1.25 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | resize_1.25 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id | resize_1.25 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | identity | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | identity | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | identity | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | identity | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | jpeg_75 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | jpeg_75 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | jpeg_75 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | jpeg_75 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | resize_0.75 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | resize_0.75 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | resize_0.75 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | resize_0.75 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | resize_1.25 | gradnoise 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | resize_1.25 | gradnoise 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | resize_1.25 | pink 320×240 | 25 | 0 | 0.0% (≤13.7%) | — |
| unmarked image | ss_id_flip | resize_1.25 | pink 640×480 | 25 | 0 | 0.0% (≤13.7%) | — |
| marked, wrong key | ss | identity | gradnoise 320×240 | 48 | 14 | 29.2% (≤44.1%) | 14 |
| marked, wrong key | ss | identity | gradnoise 640×480 | 48 | 12 | 25.0% (≤39.6%) | 12 |
| marked, wrong key | ss | identity | pink 320×240 | 48 | 2 | 4.2% (≤14.3%) | 1 |
| marked, wrong key | ss | identity | pink 640×480 | 48 | 9 | 18.8% (≤32.6%) | 9 |
| marked, wrong key | ss | jpeg_75 | gradnoise 320×240 | 48 | 12 | 25.0% (≤39.6%) | 12 |
| marked, wrong key | ss | jpeg_75 | gradnoise 640×480 | 48 | 7 | 14.6% (≤27.8%) | 7 |
| marked, wrong key | ss | jpeg_75 | pink 320×240 | 48 | 1 | 2.1% (≤11.1%) | 1 |
| marked, wrong key | ss | jpeg_75 | pink 640×480 | 48 | 8 | 16.7% (≤30.2%) | 8 |
| marked, wrong key | ss_flip | identity | gradnoise 320×240 | 48 | 20 | 41.7% (≤56.8%) | 20 |
| marked, wrong key | ss_flip | identity | gradnoise 640×480 | 48 | 18 | 37.5% (≤52.6%) | 18 |
| marked, wrong key | ss_flip | identity | pink 320×240 | 48 | 4 | 8.3% (≤20.0%) | 3 |
| marked, wrong key | ss_flip | identity | pink 640×480 | 48 | 19 | 39.6% (≤54.7%) | 19 |
| marked, wrong key | ss_flip | jpeg_75 | gradnoise 320×240 | 48 | 15 | 31.2% (≤46.3%) | 15 |
| marked, wrong key | ss_flip | jpeg_75 | gradnoise 640×480 | 48 | 18 | 37.5% (≤52.6%) | 18 |
| marked, wrong key | ss_flip | jpeg_75 | pink 320×240 | 48 | 2 | 4.2% (≤14.3%) | 2 |
| marked, wrong key | ss_flip | jpeg_75 | pink 640×480 | 48 | 17 | 35.4% (≤50.5%) | 17 |
| marked, wrong key | ss_id | identity | gradnoise 320×240 | 48 | 20 | 41.7% (≤56.8%) | 20 |
| marked, wrong key | ss_id | identity | gradnoise 640×480 | 48 | 18 | 37.5% (≤52.6%) | 18 |
| marked, wrong key | ss_id | identity | pink 320×240 | 48 | 3 | 6.2% (≤17.2%) | 3 |
| marked, wrong key | ss_id | identity | pink 640×480 | 48 | 19 | 39.6% (≤54.7%) | 19 |
| marked, wrong key | ss_id | jpeg_75 | gradnoise 320×240 | 48 | 15 | 31.2% (≤46.3%) | 15 |
| marked, wrong key | ss_id | jpeg_75 | gradnoise 640×480 | 48 | 18 | 37.5% (≤52.6%) | 18 |
| marked, wrong key | ss_id | jpeg_75 | pink 320×240 | 48 | 2 | 4.2% (≤14.3%) | 2 |
| marked, wrong key | ss_id | jpeg_75 | pink 640×480 | 48 | 17 | 35.4% (≤50.5%) | 17 |
| marked, wrong key | ss_id_flip | identity | gradnoise 320×240 | 48 | 20 | 41.7% (≤56.8%) | 20 |
| marked, wrong key | ss_id_flip | identity | gradnoise 640×480 | 48 | 18 | 37.5% (≤52.6%) | 18 |
| marked, wrong key | ss_id_flip | identity | pink 320×240 | 48 | 3 | 6.2% (≤17.2%) | 3 |
| marked, wrong key | ss_id_flip | identity | pink 640×480 | 48 | 19 | 39.6% (≤54.7%) | 19 |
| marked, wrong key | ss_id_flip | jpeg_75 | gradnoise 320×240 | 48 | 15 | 31.2% (≤46.3%) | 15 |
| marked, wrong key | ss_id_flip | jpeg_75 | gradnoise 640×480 | 48 | 18 | 37.5% (≤52.6%) | 18 |
| marked, wrong key | ss_id_flip | jpeg_75 | pink 320×240 | 48 | 2 | 4.2% (≤14.3%) | 2 |
| marked, wrong key | ss_id_flip | jpeg_75 | pink 640×480 | 48 | 17 | 35.4% (≤50.5%) | 17 |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss | 320×240 | 72 | 9 ms | 10 ms | 10 ms | 119 ms |  |
| decode:ss | 640×480 | 72 | 38 ms | 41 ms | 58 ms | 125 ms |  |
| decode:ss_flip | 320×240 | 72 | 34 ms | 35 ms | 38 ms | 445 ms |  |
| decode:ss_flip | 640×480 | 72 | 127 ms | 132 ms | 134 ms | 413 ms |  |
| decode:ss_id | 320×240 | 24 | 9 ms | 10 ms | 10 ms | 124 ms |  |
| decode:ss_id | 640×480 | 24 | 39 ms | 56 ms | 59 ms | 127 ms |  |
| decode:ss_id_flip | 320×240 | 24 | 9 ms | 10 ms | 10 ms | 123 ms |  |
| decode:ss_id_flip | 640×480 | 24 | 39 ms | 56 ms | 60 ms | 127 ms |  |
| embed:ss | 320×240 | 72 | 16 ms | 17 ms | 18 ms | 202 ms |  |
| embed:ss | 640×480 | 72 | 71 ms | 75 ms | 91 ms | 230 ms |  |
