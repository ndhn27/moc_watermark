# Watermark benchmark — `standard` suite
_2026-09-20T23:24:04+00:00 · 5552 trials in 190.3 s · seed 20260919_

wmcore fingerprint `9b526cba70a9` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: synthetic images (pink, gradnoise) — a stand-in for photos; use `--images DIR` for numbers you intend to publish.

## Headline

- **`ss` detection** over gated attacks: 765/768 = 99.6% [98.9%-99.9%]; weakest gated attack `crop_top_64` at 83.3% (n=12).
- **`ss_id` detection** over gated attacks: 768/768 = 100.0% [99.5%-100.0%]; weakest gated attack `avif_60` at 100.0% (n=12).
- **`ss` unmarked-image FPR**: 0/400 = 0.0% (95% upper bound 0.9%).
- **`ss_id` unmarked-image FPR**: 0/400 = 0.0% (95% upper bound 0.9%).
- **`ss` wrong-key acceptance**: 65/384 = 16.9% (95% upper bound 21.1%); exact payload recovered in 64/384.
- **`ss_id` wrong-key acceptance**: 112/384 = 29.2% (95% upper bound 34.0%); exact payload recovered in 112/384.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| blur_0.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| blur_1.0 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| †blur_1.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| brightness_+25 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| contrast_0.8 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| crop_top_64 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 7 ms | 7 ms |  |
| †crop_topleft_64 | 12 | 0.0% [0%–24%] | 66.7% | 0.000 | 0.000 | 6 ms | 6 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 8 ms | 9 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 8.3% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 8 ms | 9 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| gamma_1.3 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| †jpeg_30 | 12 | 75.0% [47%–91%] | 0.0% | 0.078 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| jpeg_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_85 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_95 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| †noise_10 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 9 ms |  |
| noise_2 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| noise_5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 3 ms | 3 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 5 ms | 5 ms | no oracle geometry |
| †resize_0.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 3 ms | 3 ms | signal intact - decoder loses sync |
| †resize_0.62 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 4 ms | 4 ms | signal intact - decoder loses sync |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 5 ms | 5 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 5 ms | 6 ms | signal intact - decoder loses sync |
| †resize_0.9 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 8 ms | 8 ms | signal intact - decoder loses sync |
| †resize_1.25 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 14 ms | 14 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 17 ms | 18 ms | signal intact - decoder loses sync |
| †resize_1.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 20 ms | 21 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |

#### `ss` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 46 ms |  |
| blur_0.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 53 ms |  |
| blur_1.0 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 54 ms |  |
| †blur_1.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 55 ms |  |
| brightness_+25 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 54 ms |  |
| contrast_0.8 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 58 ms |  |
| crop_top_64 | 12 | 83.3% [55%–95%] | 16.7% | 0.000 | 0.000 | 31 ms | 39 ms | signal intact - decoder loses sync |
| †crop_topleft_64 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 35 ms | 36 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 34 ms | 51 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 33.3% | n/a | n/a | 35 ms | 38 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 35 ms | 36 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 8.3% | n/a | n/a | 36 ms | 55 ms | no oracle geometry |
| gamma_1.3 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 54 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 36 ms | 46 ms |  |
| †jpeg_30 | 12 | 100.0% [76%–100%] | 0.0% | 0.086 | 0.000 | 37 ms | 46 ms |  |
| jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 45 ms |  |
| jpeg_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 36 ms | 45 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 36 ms | 45 ms |  |
| jpeg_85 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 36 ms | 45 ms |  |
| jpeg_95 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 36 ms | 46 ms |  |
| †noise_10 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 36 ms | 54 ms |  |
| noise_2 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 53 ms |  |
| noise_5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 55 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 37 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 37 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 13 ms | 19 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 20 ms | 25 ms | no oracle geometry |
| †resize_0.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 10 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.62 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 14 ms | 18 ms | signal intact - decoder loses sync |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 21 ms | 26 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 21 ms | 26 ms | signal intact - decoder loses sync |
| †resize_0.9 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 29 ms | 37 ms | signal intact - decoder loses sync |
| †resize_1.25 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 56 ms | 70 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 71 ms | 88 ms | signal intact - decoder loses sync |
| †resize_1.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 89 ms | 109 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 54 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 56 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 54 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 57 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 36 ms | 45 ms |  |

#### `ss` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 14 ms |  |
| blur_0.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.006 | 0.000 | 9 ms | 9 ms |  |
| blur_1.0 | 12 | 91.7% [65%–99%] | 0.0% | 0.026 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †blur_1.5 | 12 | 16.7% [5%–45%] | 0.0% | 0.175 | 0.010 | 9 ms | 10 ms | signal intact - decoder loses sync |
| brightness_+25 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |
| contrast_0.8 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms |  |
| crop_top_64 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 7 ms | 7 ms |  |
| †crop_topleft_64 | 12 | 0.0% [0%–24%] | 75.0% | 0.003 | 0.000 | 5 ms | 7 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 8 ms | 8 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 8 ms | 9 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| gamma_1.3 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 11 ms |  |
| †jpeg_30 | 12 | 100.0% [76%–100%] | 0.0% | 0.074 | 0.000 | 9 ms | 11 ms |  |
| jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.007 | 0.000 | 9 ms | 11 ms |  |
| jpeg_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 11 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 11 ms |  |
| jpeg_85 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 11 ms |  |
| jpeg_95 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 11 ms |  |
| †noise_10 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 10 ms |  |
| noise_2 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms |  |
| noise_5 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 9 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 3 ms | 3 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 5 ms | 5 ms | no oracle geometry |
| †resize_0.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.064 | 0.000 | 3 ms | 3 ms | signal intact - decoder loses sync |
| †resize_0.62 | 12 | 0.0% [0%–24%] | 0.0% | 0.020 | 0.000 | 4 ms | 5 ms | signal intact - decoder loses sync |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.008 | 0.000 | 5 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.014 | 0.000 | 5 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.9 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 7 ms | 11 ms | signal intact - decoder loses sync |
| †resize_1.25 | 12 | 0.0% [0%–24%] | 0.0% | 0.005 | 0.000 | 14 ms | 21 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 17 ms | 24 ms | signal intact - decoder loses sync |
| †resize_1.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 20 ms | 31 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 11 ms |  |

#### `ss` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 36 ms | 40 ms |  |
| blur_0.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 37 ms | 46 ms |  |
| blur_1.0 | 12 | 100.0% [76%–100%] | 0.0% | 0.025 | 0.000 | 37 ms | 50 ms |  |
| †blur_1.5 | 12 | 50.0% [25%–75%] | 0.0% | 0.139 | 0.000 | 36 ms | 38 ms | signal intact - decoder loses sync |
| brightness_+25 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 36 ms | 38 ms |  |
| contrast_0.8 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 56 ms |  |
| crop_top_64 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 32 ms | 38 ms |  |
| †crop_topleft_64 | 12 | 0.0% [0%–24%] | 8.3% | 0.003 | 0.000 | 28 ms | 37 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 35 ms | 39 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 34 ms | 36 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 8.3% | n/a | n/a | 36 ms | 48 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 35 ms | 37 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 46 ms | no oracle geometry |
| gamma_1.3 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 36 ms | 38 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 40 ms |  |
| †jpeg_30 | 12 | 91.7% [65%–99%] | 8.3% | 0.099 | 0.000 | 37 ms | 38 ms | signal intact - decoder loses sync |
| jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.006 | 0.000 | 37 ms | 39 ms |  |
| jpeg_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 37 ms | 39 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 39 ms |  |
| jpeg_85 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 36 ms | 39 ms |  |
| jpeg_95 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 39 ms |  |
| †noise_10 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 37 ms | 37 ms |  |
| noise_2 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 45 ms |  |
| noise_5 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 36 ms | 46 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 46 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 44 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 13 ms | 13 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 20 ms | 21 ms | no oracle geometry |
| †resize_0.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.060 | 0.000 | 10 ms | 10 ms | signal intact - decoder loses sync |
| †resize_0.62 | 12 | 0.0% [0%–24%] | 0.0% | 0.020 | 0.000 | 14 ms | 14 ms | signal intact - decoder loses sync |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.007 | 0.000 | 20 ms | 21 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.012 | 0.000 | 21 ms | 22 ms | signal intact - decoder loses sync |
| †resize_0.9 | 12 | 0.0% [0%–24%] | 0.0% | 0.005 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †resize_1.25 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 57 ms | 59 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 71 ms | 76 ms | signal intact - decoder loses sync |
| †resize_1.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 89 ms | 90 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 56 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 56 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 56 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 38 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 39 ms |  |

#### `ss_id` · gradnoise 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| blur_0.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| blur_1.0 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| †blur_1.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| brightness_+25 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| contrast_0.8 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| crop_top_64 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 7 ms | 7 ms |  |
| †crop_topleft_64 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 6 ms | 6 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| gamma_1.3 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| †jpeg_30 | 12 | 100.0% [76%–100%] | 0.0% | 0.078 | 0.000 | 10 ms | 10 ms |  |
| jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| jpeg_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_85 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 9 ms | 10 ms |  |
| jpeg_95 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| †noise_10 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| noise_2 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| noise_5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 4 ms | 4 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 5 ms | 6 ms | no oracle geometry |
| †resize_0.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 3 ms | 3 ms | signal intact - decoder loses sync |
| †resize_0.62 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 4 ms | 4 ms | signal intact - decoder loses sync |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 6 ms | 6 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 6 ms | 6 ms | signal intact - decoder loses sync |
| †resize_0.9 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 8 ms | 8 ms | signal intact - decoder loses sync |
| †resize_1.25 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 14 ms | 15 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 18 ms | 22 ms | signal intact - decoder loses sync |
| †resize_1.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 21 ms | 22 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 10 ms | 10 ms |  |

#### `ss_id` · gradnoise 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 46 ms |  |
| blur_0.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 55 ms |  |
| blur_1.0 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 56 ms |  |
| †blur_1.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 54 ms |  |
| brightness_+25 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 56 ms |  |
| contrast_0.8 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 52 ms |  |
| crop_top_64 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 32 ms | 41 ms |  |
| †crop_topleft_64 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 35 ms | 52 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 54 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 39 ms | no oracle geometry |
| gamma_1.3 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 56 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 45 ms |  |
| †jpeg_30 | 12 | 100.0% [76%–100%] | 0.0% | 0.086 | 0.000 | 37 ms | 46 ms |  |
| jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 46 ms |  |
| jpeg_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 46 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 45 ms |  |
| jpeg_85 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 45 ms |  |
| jpeg_95 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 46 ms |  |
| †noise_10 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 53 ms |  |
| noise_2 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 54 ms |  |
| noise_5 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 56 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 38 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 38 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 13 ms | 20 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 20 ms | 21 ms | no oracle geometry |
| †resize_0.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 10 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.62 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 14 ms | 17 ms | signal intact - decoder loses sync |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 21 ms | 26 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 21 ms | 26 ms | signal intact - decoder loses sync |
| †resize_0.9 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 30 ms | 37 ms | signal intact - decoder loses sync |
| †resize_1.25 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 57 ms | 71 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 72 ms | 90 ms | signal intact - decoder loses sync |
| †resize_1.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.000 | 0.000 | 90 ms | 110 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 54 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 54 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 56 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 56 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.000 | 0.000 | 37 ms | 46 ms |  |

#### `ss_id` · pink 320×240 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 14 ms |  |
| blur_0.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.006 | 0.000 | 10 ms | 10 ms |  |
| blur_1.0 | 12 | 100.0% [76%–100%] | 0.0% | 0.026 | 0.000 | 9 ms | 10 ms |  |
| †blur_1.5 | 12 | 50.0% [25%–75%] | 0.0% | 0.175 | 0.010 | 9 ms | 10 ms | signal intact - decoder loses sync |
| brightness_+25 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |
| contrast_0.8 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |
| crop_top_64 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 7 ms | 7 ms |  |
| †crop_topleft_64 | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 6 ms | 6 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 8 ms | 10 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| gamma_1.3 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 12 ms |  |
| †jpeg_30 | 12 | 100.0% [76%–100%] | 0.0% | 0.074 | 0.000 | 10 ms | 12 ms |  |
| jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.007 | 0.000 | 9 ms | 12 ms |  |
| jpeg_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 12 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 9 ms | 12 ms |  |
| jpeg_85 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 10 ms | 12 ms |  |
| jpeg_95 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 12 ms |  |
| †noise_10 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 10 ms |  |
| noise_2 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |
| noise_5 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 9 ms | 10 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 4 ms | 4 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 5 ms | 6 ms | no oracle geometry |
| †resize_0.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.064 | 0.000 | 3 ms | 4 ms | signal intact - decoder loses sync |
| †resize_0.62 | 12 | 0.0% [0%–24%] | 0.0% | 0.020 | 0.000 | 4 ms | 6 ms | signal intact - decoder loses sync |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.008 | 0.000 | 6 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.014 | 0.000 | 6 ms | 7 ms | signal intact - decoder loses sync |
| †resize_0.9 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 8 ms | 11 ms | signal intact - decoder loses sync |
| †resize_1.25 | 12 | 0.0% [0%–24%] | 0.0% | 0.005 | 0.000 | 14 ms | 22 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 18 ms | 19 ms | signal intact - decoder loses sync |
| †resize_1.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 21 ms | 31 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 9 ms | 10 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 10 ms | 12 ms |  |

#### `ss_id` · pink 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 37 ms | 38 ms |  |
| blur_0.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.005 | 0.000 | 37 ms | 46 ms |  |
| blur_1.0 | 12 | 100.0% [76%–100%] | 0.0% | 0.025 | 0.000 | 37 ms | 37 ms |  |
| †blur_1.5 | 12 | 100.0% [76%–100%] | 0.0% | 0.139 | 0.000 | 37 ms | 38 ms |  |
| brightness_+25 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 39 ms |  |
| contrast_0.8 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 46 ms |  |
| crop_top_64 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 32 ms | 34 ms |  |
| †crop_topleft_64 | 12 | 0.0% [0%–24%] | 0.0% | 0.003 | 0.000 | 29 ms | 37 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 38 ms | no oracle geometry |
| †crop_unaligned_15 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 35 ms | 36 ms | no oracle geometry |
| †crop_unaligned_3 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 39 ms | no oracle geometry |
| †crop_unaligned_7 | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 36 ms | 38 ms | no oracle geometry |
| †flip_horizontal | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 47 ms | no oracle geometry |
| gamma_1.3 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 46 ms |  |
| identity | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 39 ms |  |
| †jpeg_30 | 12 | 100.0% [76%–100%] | 0.0% | 0.099 | 0.000 | 37 ms | 39 ms |  |
| jpeg_50 | 12 | 100.0% [76%–100%] | 0.0% | 0.006 | 0.000 | 37 ms | 39 ms |  |
| jpeg_60 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 37 ms | 39 ms |  |
| jpeg_75 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 40 ms |  |
| jpeg_85 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 38 ms |  |
| jpeg_95 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 40 ms |  |
| †noise_10 | 12 | 100.0% [76%–100%] | 0.0% | 0.004 | 0.000 | 37 ms | 38 ms |  |
| noise_2 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 40 ms |  |
| noise_5 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 56 ms |  |
| †perspective_light | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †perspective_medium | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 46 ms | no oracle geometry |
| †pipeline_heavy_repost | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 13 ms | 13 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 20 ms | 21 ms | no oracle geometry |
| †resize_0.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.060 | 0.000 | 10 ms | 10 ms | signal intact - decoder loses sync |
| †resize_0.62 | 12 | 0.0% [0%–24%] | 0.0% | 0.020 | 0.000 | 14 ms | 14 ms | signal intact - decoder loses sync |
| †resize_0.75 | 12 | 0.0% [0%–24%] | 0.0% | 0.007 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.012 | 0.000 | 21 ms | 22 ms | signal intact - decoder loses sync |
| †resize_0.9 | 12 | 0.0% [0%–24%] | 0.0% | 0.005 | 0.000 | 30 ms | 31 ms | signal intact - decoder loses sync |
| †resize_1.25 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 57 ms | 58 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 12 | 0.0% [0%–24%] | 0.0% | 0.006 | 0.000 | 72 ms | 77 ms | signal intact - decoder loses sync |
| †resize_1.5 | 12 | 0.0% [0%–24%] | 0.0% | 0.004 | 0.000 | 90 ms | 91 ms | signal intact - decoder loses sync |
| †rotate_1deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 56 ms | no oracle geometry |
| †rotate_2deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 56 ms | no oracle geometry |
| †rotate_3deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 46 ms | no oracle geometry |
| †rotate_5deg | 12 | 0.0% [0%–24%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| webp_80 | 12 | 100.0% [76%–100%] | 0.0% | 0.003 | 0.000 | 37 ms | 39 ms |  |

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
| marked, wrong key | ss | identity | gradnoise 320×240 | 48 | 14 | 29.2% (≤44.1%) | 14 |
| marked, wrong key | ss | identity | gradnoise 640×480 | 48 | 12 | 25.0% (≤39.6%) | 12 |
| marked, wrong key | ss | identity | pink 320×240 | 48 | 2 | 4.2% (≤14.3%) | 1 |
| marked, wrong key | ss | identity | pink 640×480 | 48 | 9 | 18.8% (≤32.6%) | 9 |
| marked, wrong key | ss | jpeg_75 | gradnoise 320×240 | 48 | 12 | 25.0% (≤39.6%) | 12 |
| marked, wrong key | ss | jpeg_75 | gradnoise 640×480 | 48 | 7 | 14.6% (≤27.8%) | 7 |
| marked, wrong key | ss | jpeg_75 | pink 320×240 | 48 | 1 | 2.1% (≤11.1%) | 1 |
| marked, wrong key | ss | jpeg_75 | pink 640×480 | 48 | 8 | 16.7% (≤30.2%) | 8 |
| marked, wrong key | ss_id | identity | gradnoise 320×240 | 48 | 20 | 41.7% (≤56.8%) | 20 |
| marked, wrong key | ss_id | identity | gradnoise 640×480 | 48 | 18 | 37.5% (≤52.6%) | 18 |
| marked, wrong key | ss_id | identity | pink 320×240 | 48 | 3 | 6.2% (≤17.2%) | 3 |
| marked, wrong key | ss_id | identity | pink 640×480 | 48 | 19 | 39.6% (≤54.7%) | 19 |
| marked, wrong key | ss_id | jpeg_75 | gradnoise 320×240 | 48 | 15 | 31.2% (≤46.3%) | 15 |
| marked, wrong key | ss_id | jpeg_75 | gradnoise 640×480 | 48 | 18 | 37.5% (≤52.6%) | 18 |
| marked, wrong key | ss_id | jpeg_75 | pink 320×240 | 48 | 2 | 4.2% (≤14.3%) | 2 |
| marked, wrong key | ss_id | jpeg_75 | pink 640×480 | 48 | 17 | 35.4% (≤50.5%) | 17 |

## Runtime

| operation | size | n | p50 | p95 | max | p50 per MP | budget hit |
|---|---|---|---|---|---|---|---|
| decode:ss | 320×240 | 24 | 9 ms | 10 ms | 14 ms | 119 ms |  |
| decode:ss | 640×480 | 24 | 36 ms | 42 ms | 55 ms | 119 ms |  |
| decode:ss_id | 320×240 | 24 | 10 ms | 10 ms | 14 ms | 124 ms |  |
| decode:ss_id | 640×480 | 24 | 37 ms | 40 ms | 55 ms | 119 ms |  |
| embed:ss | 320×240 | 24 | 16 ms | 18 ms | 20 ms | 204 ms |  |
| embed:ss | 640×480 | 24 | 73 ms | 78 ms | 84 ms | 237 ms |  |
