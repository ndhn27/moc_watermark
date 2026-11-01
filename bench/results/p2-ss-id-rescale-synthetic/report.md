# Watermark benchmark — `standard` suite
_2026-09-21T10:03:00+00:00 · 816 trials in 255.8 s · seed 20260919_

wmcore fingerprint `b62d785325a9` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss_rescale` detection** over gated attacks: 182/192 = 94.8% [90.7%-97.1%]; weakest gated attack `resize_0.62` at 33.3% (n=6).
- **`ss_id_rescale` detection** over gated attacks: 187/192 = 97.4% [94.0%-98.9%]; weakest gated attack `resize_0.62` at 33.3% (n=6).
- **`ss_or_id_rescale` detection** over gated attacks: 187/192 = 97.4% [94.0%-98.9%]; weakest gated attack `resize_0.62` at 33.3% (n=6).
- **`ss_rescale` unmarked-image FPR**: 0/48 = 0.0% (95% upper bound 7.4%).
- **`ss_id_rescale` unmarked-image FPR**: 0/48 = 0.0% (95% upper bound 7.4%).
- **`ss_or_id_rescale` unmarked-image FPR**: 0/48 = 0.0% (95% upper bound 7.4%).
- **`ss_rescale` runtime** on resized images it can recover: median of per-attack p50 = 1.7 s.
- **`ss_id_rescale` runtime** on resized images it can recover: median of per-attack p50 = 1.6 s.
- **`ss_or_id_rescale` runtime** on resized images it can recover: median of per-attack p50 = 1.7 s.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss_id_rescale` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms | 0.97 | n/a |  |  |
| †resize_0.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 460 ms | 490 ms | 0.80 | 0.0016 |  |  |
| resize_0.62 | 6 | 83.3% [44%–97%] | 0.0% | 0.000 | 0.000 | 710 ms | 758 ms | 0.81 | 0.0036 |  | signal intact - decoder loses sync |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 956 ms | 1.0 s | 0.80 | 0.0016 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 944 ms | 971 ms | 0.81 | 0.0016 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.1 s | 1.2 s | 0.80 | 0.0016 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.5 s | 1.7 s | 0.80 | 0.0016 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.6 s | 1.7 s | 0.80 | 0.0016 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.6 s | 1.8 s | 0.80 | 0.0016 |  |  |

#### `ss_id_rescale` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 31 ms | 33 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.6 s | 1.7 s | 0.84 | 0.0008 |  |  |
| resize_0.62 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.9 s | 2.1 s | 0.84 | 0.0003 |  |  |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.9 s | 2.0 s | 0.83 | 0.0008 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.1 s | 2.4 s | 0.83 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.1 s | 2.2 s | 0.83 | 0.0008 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.3 s | 0.83 | 0.0008 |  |  |

#### `ss_id_rescale` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 10 ms | 0.97 | n/a |  |  |
| †resize_0.5 | 6 | 83.3% [44%–97%] | 0.0% | 0.048 | 0.000 | 448 ms | 468 ms | 0.79 | 0.0016 |  | signal intact - decoder loses sync |
| resize_0.62 | 6 | 33.3% [10%–70%] | 0.0% | 0.015 | 0.000 | 711 ms | 855 ms | 0.80 | 0.0036 |  | signal intact - decoder loses sync |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.007 | 0.000 | 903 ms | 997 ms | 0.80 | 0.0016 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.012 | 0.000 | 923 ms | 957 ms | 0.80 | 0.0016 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.007 | 0.000 | 1.1 s | 1.2 s | 0.80 | 0.0016 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 1.5 s | 1.7 s | 0.80 | 0.0016 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 1.6 s | 1.7 s | 0.80 | 0.0016 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 1.6 s | 1.6 s | 0.80 | 0.0016 |  |  |

#### `ss_id_rescale` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.004 | 0.000 | 33 ms | 34 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.052 | 0.000 | 1.6 s | 4.1 s | 0.78 | 0.0008 |  |  |
| resize_0.62 | 6 | 100.0% [61%–100%] | 0.0% | 0.019 | 0.000 | 1.9 s | 2.0 s | 0.79 | 0.0003 |  |  |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.008 | 0.000 | 2.1 s | 2.2 s | 0.80 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.012 | 0.000 | 2.0 s | 2.4 s | 0.80 | 0.0008 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 2.0 s | 2.2 s | 0.81 | 0.0008 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 2.1 s | 2.2 s | 0.83 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 2.0 s | 2.2 s | 0.83 | 0.0008 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 2.1 s | 2.3 s | 0.83 | 0.0008 |  |  |

#### `ss_or_id_rescale` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms | 0.97 | n/a |  |  |
| †resize_0.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 464 ms | 510 ms | 0.80 | 0.0016 |  |  |
| resize_0.62 | 6 | 83.3% [44%–97%] | 0.0% | 0.000 | 0.000 | 741 ms | 780 ms | 0.81 | 0.0036 |  | signal intact - decoder loses sync |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 950 ms | 1.0 s | 0.80 | 0.0016 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 952 ms | 978 ms | 0.81 | 0.0016 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.1 s | 1.3 s | 0.80 | 0.0016 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.5 s | 1.7 s | 0.80 | 0.0016 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.6 s | 1.7 s | 0.80 | 0.0016 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.7 s | 1.8 s | 0.80 | 0.0016 |  |  |

#### `ss_or_id_rescale` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 32 ms | 34 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.6 s | 1.7 s | 0.84 | 0.0008 |  |  |
| resize_0.62 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.9 s | 2.0 s | 0.84 | 0.0003 |  |  |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.1 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.2 s | 0.83 | 0.0008 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.1 s | 2.2 s | 0.83 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.1 s | 2.2 s | 0.83 | 0.0008 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.1 s | 2.1 s | 0.83 | 0.0008 |  |  |

#### `ss_or_id_rescale` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 10 ms | 0.97 | n/a |  |  |
| †resize_0.5 | 6 | 83.3% [44%–97%] | 0.0% | 0.048 | 0.000 | 453 ms | 481 ms | 0.79 | 0.0016 |  | signal intact - decoder loses sync |
| resize_0.62 | 6 | 33.3% [10%–70%] | 0.0% | 0.015 | 0.000 | 704 ms | 824 ms | 0.80 | 0.0036 |  | signal intact - decoder loses sync |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.007 | 0.000 | 902 ms | 948 ms | 0.80 | 0.0016 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.012 | 0.000 | 890 ms | 926 ms | 0.80 | 0.0016 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.007 | 0.000 | 1.1 s | 1.1 s | 0.80 | 0.0016 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 1.5 s | 1.6 s | 0.80 | 0.0016 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 1.7 s | 1.7 s | 0.80 | 0.0016 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 1.6 s | 1.8 s | 0.80 | 0.0016 |  |  |

#### `ss_or_id_rescale` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.004 | 0.000 | 32 ms | 34 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.052 | 0.000 | 1.6 s | 4.3 s | 0.78 | 0.0008 |  |  |
| resize_0.62 | 6 | 100.0% [61%–100%] | 0.0% | 0.019 | 0.000 | 1.9 s | 1.9 s | 0.79 | 0.0003 |  |  |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.008 | 0.000 | 2.0 s | 2.1 s | 0.80 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.012 | 0.000 | 2.0 s | 2.1 s | 0.80 | 0.0008 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 2.0 s | 2.1 s | 0.81 | 0.0008 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 2.1 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 2.0 s | 2.2 s | 0.83 | 0.0008 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 2.1 s | 2.2 s | 0.83 | 0.0008 |  |  |

#### `ss_rescale` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 8 ms | 9 ms | 0.97 | n/a |  |  |
| †resize_0.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 463 ms | 473 ms | 0.80 | 0.0016 |  |  |
| resize_0.62 | 6 | 83.3% [44%–97%] | 0.0% | 0.000 | 0.000 | 739 ms | 779 ms | 0.81 | 0.0036 |  | signal intact - decoder loses sync |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 942 ms | 974 ms | 0.80 | 0.0016 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 952 ms | 1.0 s | 0.81 | 0.0016 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.1 s | 1.2 s | 0.80 | 0.0016 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.6 s | 1.6 s | 0.80 | 0.0016 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.7 s | 1.7 s | 0.80 | 0.0016 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.7 s | 1.7 s | 0.80 | 0.0016 |  |  |

#### `ss_rescale` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 31 ms | 33 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.6 s | 1.7 s | 0.84 | 0.0008 |  |  |
| resize_0.62 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.9 s | 2.0 s | 0.84 | 0.0003 |  |  |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 1.9 s | 2.0 s | 0.83 | 0.0008 |  |  |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.000 | 0.000 | 2.1 s | 2.1 s | 0.83 | 0.0008 |  |  |

#### `ss_rescale` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 9 ms | 0.97 | n/a |  |  |
| †resize_0.5 | 6 | 50.0% [19%–81%] | 0.0% | 0.048 | 0.000 | 464 ms | 501 ms | 0.79 | 0.0016 |  | signal intact - decoder loses sync |
| resize_0.62 | 6 | 33.3% [10%–70%] | 0.0% | 0.015 | 0.000 | 690 ms | 809 ms | 0.80 | 0.0036 |  | signal intact - decoder loses sync |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.007 | 0.000 | 907 ms | 1.0 s | 0.80 | 0.0016 |  |  |
| resize_0.75_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.012 | 0.000 | 899 ms | 912 ms | 0.80 | 0.0016 |  |  |
| resize_0.9 | 6 | 83.3% [44%–97%] | 0.0% | 0.007 | 0.000 | 1.2 s | 2.9 s | 0.80 | 0.0016 |  | signal intact - decoder loses sync |
| resize_1.25 | 6 | 83.3% [44%–97%] | 0.0% | 0.005 | 0.000 | 1.5 s | 5.7 s | 0.80 | 0.0016 |  | signal intact - decoder loses sync |
| resize_1.4_jpeg85 | 6 | 83.3% [44%–97%] | 0.0% | 0.006 | 0.000 | 1.6 s | 6.1 s | 0.80 | 0.0016 |  | signal intact - decoder loses sync |
| resize_1.5 | 6 | 83.3% [44%–97%] | 0.0% | 0.006 | 0.000 | 1.7 s | 6.8 s | 0.80 | 0.0016 |  | signal intact - decoder loses sync |

#### `ss_rescale` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | confidence | scale err | budget hit | reading |
|---|---|---|---|---|---|---|---|---|---|---|---|
| identity | 6 | 100.0% [61%–100%] | 0.0% | 0.004 | 0.000 | 32 ms | 34 ms | 1.00 | n/a |  |  |
| †resize_0.5 | 6 | 83.3% [44%–97%] | 0.0% | 0.052 | 0.000 | 1.7 s | 3.9 s | 0.78 | 0.0008 |  | signal intact - decoder loses sync |
| resize_0.62 | 6 | 100.0% [61%–100%] | 0.0% | 0.019 | 0.000 | 1.9 s | 1.9 s | 0.79 | 0.0003 |  |  |
| resize_0.75 | 6 | 100.0% [61%–100%] | 0.0% | 0.008 | 0.000 | 2.0 s | 2.0 s | 0.80 | 0.0008 |  |  |
| resize_0.75_jpeg85 | 6 | 83.3% [44%–97%] | 0.0% | 0.012 | 0.000 | 2.0 s | 6.9 s | 0.80 | 0.0008 |  | signal intact - decoder loses sync |
| resize_0.9 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 2.0 s | 2.1 s | 0.81 | 0.0008 |  |  |
| resize_1.25 | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_1.4_jpeg85 | 6 | 100.0% [61%–100%] | 0.0% | 0.006 | 0.000 | 2.0 s | 2.1 s | 0.83 | 0.0008 |  |  |
| resize_1.5 | 6 | 100.0% [61%–100%] | 0.0% | 0.005 | 0.000 | 2.1 s | 2.1 s | 0.83 | 0.0008 |  |  |

## False positives

Any text returned counts. With n images the smallest FPR that can be claimed is about 3/n (rule of three) — the upper bound, not the point estimate, is the honest figure.

| condition | decoder | attack | images | n | FP | FPR (95% upper) | payload recovered |
|---|---|---|---|---|---|---|---|
| unmarked image | ss_id_rescale | identity | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | identity | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | identity | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | identity | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | resize_0.75 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_id_rescale | resize_1.25 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | identity | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | identity | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | identity | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | identity | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | resize_0.75 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_or_id_rescale | resize_1.25 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | identity | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | identity | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | identity | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | identity | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | resize_0.75 | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | resize_0.75 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | resize_0.75 | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | resize_0.75 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | resize_1.25 | gradnoise 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | resize_1.25 | gradnoise 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | resize_1.25 | pink 320×240 | 4 | 0 | 0.0% (≤60.2%) | — |
| unmarked image | ss_rescale | resize_1.25 | pink 640×480 | 4 | 0 | 0.0% (≤60.2%) | — |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss_id_rescale | 320×240 | 12 | 9 ms | 10 ms | 10 ms | 115 ms |  |
| decode:ss_id_rescale | 640×480 | 12 | 32 ms | 34 ms | 34 ms | 103 ms |  |
| decode:ss_or_id_rescale | 320×240 | 12 | 9 ms | 10 ms | 10 ms | 115 ms |  |
| decode:ss_or_id_rescale | 640×480 | 12 | 32 ms | 34 ms | 34 ms | 105 ms |  |
| decode:ss_rescale | 320×240 | 12 | 8 ms | 9 ms | 10 ms | 109 ms |  |
| decode:ss_rescale | 640×480 | 12 | 31 ms | 34 ms | 34 ms | 102 ms |  |
| embed:ss | 320×240 | 12 | 15 ms | 16 ms | 16 ms | 191 ms |  |
| embed:ss | 640×480 | 12 | 62 ms | 68 ms | 71 ms | 201 ms |  |
| rescale search [ss_id_rescale], mark found | 320×240 | 90 | 1.1 s | 1.7 s | 1.8 s | 18.7 s |  |
| rescale search [ss_id_rescale], mark found | 640×480 | 96 | 2.0 s | 2.3 s | 4.9 s | 9.9 s |  |
| rescale search [ss_id_rescale], mark missed | 320×240 | 6 | 721 ms | 863 ms | 898 ms | 24.6 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 320×240 | 24 | 4.6 s | 6.8 s | 6.8 s | 55.8 s |  |
| rescale search [ss_id_rescale], unmarked (nothing to find) | 640×480 | 24 | 10.6 s | 13.2 s | 13.8 s | 34.4 s |  |
| rescale search [ss_or_id_rescale], mark found | 320×240 | 90 | 1.1 s | 1.7 s | 1.8 s | 18.6 s |  |
| rescale search [ss_or_id_rescale], mark found | 640×480 | 96 | 2.0 s | 2.2 s | 5.2 s | 9.7 s |  |
| rescale search [ss_or_id_rescale], mark missed | 320×240 | 6 | 717 ms | 828 ms | 850 ms | 25.2 s |  |
| rescale search [ss_or_id_rescale], unmarked (nothing to find) | 320×240 | 24 | 4.5 s | 6.9 s | 6.9 s | 56.4 s |  |
| rescale search [ss_or_id_rescale], unmarked (nothing to find) | 640×480 | 24 | 10.7 s | 13.1 s | 13.8 s | 34.9 s |  |
| rescale search, mark found | 320×240 | 84 | 1.1 s | 1.7 s | 1.8 s | 19.2 s |  |
| rescale search, mark found | 640×480 | 94 | 2.0 s | 2.1 s | 2.1 s | 8.4 s |  |
| rescale search, mark missed | 320×240 | 12 | 743 ms | 8.0 s | 8.5 s | 26.5 s |  |
| rescale search, mark missed | 640×480 | 2 | 6.6 s | 8.3 s | 8.5 s | 55.0 s |  |
| rescale search, unmarked (nothing to find) | 320×240 | 24 | 4.6 s | 6.8 s | 6.8 s | 56.4 s |  |
| rescale search, unmarked (nothing to find) | 640×480 | 24 | 10.7 s | 13.0 s | 13.7 s | 34.9 s |  |
