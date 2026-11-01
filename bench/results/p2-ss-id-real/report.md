# Watermark benchmark — `standard` suite
_2026-09-20T23:27:26+00:00 · 973 trials in 72.4 s · seed 20260919_

wmcore fingerprint `9b526cba70a9` · Python 3.12.3 · numpy 2.4.4 · OpenCV 4.13.0 · Pillow 12.1.1 · x86_64, 1 CPU(s) · jobs=1

Corpus: real images from `/home/claude/realimgs`.

## Headline

- **`ss` detection** over gated attacks: 112/112 = 100.0% [96.7%-100.0%]; weakest gated attack `avif_60` at 100.0% (n=1).
- **`ss_id` detection** over gated attacks: 112/112 = 100.0% [96.7%-100.0%]; weakest gated attack `avif_60` at 100.0% (n=1).
- **`ss` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss_id` unmarked-image FPR**: 0/28 = 0.0% (95% upper bound 12.3%).
- **`ss` wrong-key acceptance**: 37/168 = 22.0% (95% upper bound 29.1%); exact payload recovered in 35/168.
- **`ss_id` wrong-key acceptance**: 41/168 = 24.4% (95% upper bound 31.6%); exact payload recovered in 41/168.

## Detection and BER  (marked → attacked → decoded)

`detect` = exact payload recovered. `misdecode` = a *different* text returned. `BER raw` / `BER comb` use oracle alignment (see bench/README.md): they measure surviving signal, not decoder success. † = not gated (a documented limit, or outside that decoder's design scope), still measured. `reading` is a heuristic for rows below 95%.

#### `ss` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 199 ms | 199 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 183 ms | 183 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 181 ms | 181 ms |  |
| †blur_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.216 | 0.000 | 181 ms | 181 ms |  |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 180 ms | 180 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 174 ms | 174 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 168 ms | 168 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 152 ms | 152 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 186 ms | 186 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 169 ms | 169 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 168 ms | 168 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 171 ms | 171 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 176 ms | 176 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 174 ms | 174 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 183 ms | 183 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.093 | 0.000 | 179 ms | 179 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.013 | 0.000 | 183 ms | 183 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 177 ms | 177 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 183 ms | 183 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 175 ms | 175 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 186 ms | 186 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 174 ms | 174 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 175 ms | 175 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 176 ms | 176 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 176 ms | 176 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 176 ms | 176 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 67 ms | 67 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 105 ms | 105 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.105 | 0.000 | 41 ms | 41 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.031 | 0.000 | 63 ms | 63 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.011 | 0.000 | 99 ms | 99 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.022 | 0.000 | 99 ms | 99 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 139 ms | 139 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 284 ms | 284 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 353 ms | 353 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 430 ms | 430 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 178 ms | 178 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 174 ms | 174 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 176 ms | 176 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 172 ms | 172 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 178 ms | 178 ms |  |

#### `ss` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.049 | 0.000 | 20 ms | 20 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.058 | 0.000 | 20 ms | 20 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.102 | 0.000 | 20 ms | 20 ms |  |
| †blur_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.269 | 0.089 | 20 ms | 20 ms | signal degraded |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.060 | 0.000 | 20 ms | 20 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.056 | 0.000 | 17 ms | 17 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.060 | 0.000 | 15 ms | 15 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 18 ms | 18 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 19 ms | 19 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.062 | 0.000 | 20 ms | 20 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms |  |
| †jpeg_30 | 1 | 0.0% [0%–79%] | 0.0% | 0.165 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.058 | 0.000 | 21 ms | 21 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.058 | 0.000 | 21 ms | 21 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 21 ms | 21 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.051 | 0.000 | 21 ms | 21 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 21 ms | 21 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 20 ms | 20 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.049 | 0.000 | 21 ms | 21 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 20 ms | 20 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 7 ms | 7 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 12 ms | 12 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 5 ms | 5 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.087 | 0.000 | 8 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.064 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.074 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.064 | 0.000 | 17 ms | 17 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.059 | 0.000 | 31 ms | 31 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.063 | 0.000 | 39 ms | 39 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.059 | 0.000 | 45 ms | 45 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.054 | 0.000 | 20 ms | 20 ms |  |

#### `ss` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 29 ms | 29 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 30 ms | 30 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.025 | 0.000 | 29 ms | 29 ms |  |
| †blur_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.118 | 0.000 | 30 ms | 30 ms |  |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 26 ms | 26 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 22 ms | 22 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 27 ms | 27 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 28 ms | 28 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 30 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.102 | 0.000 | 29 ms | 29 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.008 | 0.000 | 30 ms | 30 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 29 ms | 29 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 33 ms | 33 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 30 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 29 ms | 29 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 16 ms | 16 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.050 | 0.000 | 8 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.021 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.008 | 0.000 | 18 ms | 18 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.018 | 0.000 | 17 ms | 17 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 24 ms | 24 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 47 ms | 47 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 57 ms | 57 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 66 ms | 66 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 30 ms | 30 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 30 ms | 30 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 30 ms |  |

#### `ss` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 32 ms | 32 ms |  |
| blur_0.5 | 2 | 100.0% [34%–100%] | 0.0% | 0.031 | 0.000 | 39 ms | 45 ms |  |
| blur_1.0 | 2 | 100.0% [34%–100%] | 0.0% | 0.074 | 0.000 | 31 ms | 32 ms |  |
| †blur_1.5 | 2 | 50.0% [9%–91%] | 0.0% | 0.185 | 0.009 | 31 ms | 32 ms | signal intact - decoder loses sync |
| brightness_+25 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 32 ms | 32 ms |  |
| contrast_0.8 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 32 ms | 32 ms |  |
| crop_top_64 | 2 | 100.0% [34%–100%] | 0.0% | 0.021 | 0.000 | 27 ms | 27 ms |  |
| †crop_topleft_64 | 2 | 0.0% [0%–66%] | 0.0% | 0.021 | 0.000 | 25 ms | 25 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †crop_unaligned_15 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 30 ms | 30 ms | no oracle geometry |
| †crop_unaligned_3 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 30 ms | 30 ms | no oracle geometry |
| †crop_unaligned_7 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| gamma_1.3 | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 32 ms | 32 ms |  |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 32 ms | 32 ms |  |
| †jpeg_30 | 2 | 100.0% [34%–100%] | 0.0% | 0.093 | 0.000 | 32 ms | 32 ms |  |
| jpeg_50 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 32 ms | 32 ms |  |
| jpeg_60 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 32 ms | 32 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 31 ms | 32 ms |  |
| jpeg_85 | 2 | 100.0% [34%–100%] | 0.0% | 0.024 | 0.000 | 32 ms | 32 ms |  |
| jpeg_95 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 32 ms | 33 ms |  |
| †noise_10 | 2 | 100.0% [34%–100%] | 0.0% | 0.028 | 0.000 | 32 ms | 32 ms |  |
| noise_2 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 33 ms | 34 ms |  |
| noise_5 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 32 ms | 32 ms |  |
| †perspective_light | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| †perspective_medium | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †pipeline_heavy_repost | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 11 ms | 11 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 17 ms | 18 ms | no oracle geometry |
| †resize_0.5 | 2 | 0.0% [0%–66%] | 0.0% | 0.119 | 0.000 | 8 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.62 | 2 | 0.0% [0%–66%] | 0.0% | 0.064 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.75 | 2 | 0.0% [0%–66%] | 0.0% | 0.039 | 0.000 | 18 ms | 18 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 2 | 0.0% [0%–66%] | 0.0% | 0.046 | 0.000 | 18 ms | 18 ms | signal intact - decoder loses sync |
| †resize_0.9 | 2 | 0.0% [0%–66%] | 0.0% | 0.034 | 0.000 | 25 ms | 25 ms | signal intact - decoder loses sync |
| †resize_1.25 | 2 | 0.0% [0%–66%] | 0.0% | 0.030 | 0.000 | 49 ms | 49 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 2 | 0.0% [0%–66%] | 0.0% | 0.034 | 0.000 | 60 ms | 60 ms | signal intact - decoder loses sync |
| †resize_1.5 | 2 | 0.0% [0%–66%] | 0.0% | 0.031 | 0.000 | 70 ms | 70 ms | signal intact - decoder loses sync |
| †rotate_1deg | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 32 ms | 32 ms | no oracle geometry |
| †rotate_2deg | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 32 ms | 32 ms | no oracle geometry |
| †rotate_3deg | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| †rotate_5deg | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| webp_80 | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms |  |

#### `ss` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 37 ms | 37 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.126 | 0.000 | 36 ms | 36 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.178 | 0.000 | 37 ms | 37 ms |  |
| †blur_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.292 | 0.000 | 37 ms | 37 ms | signal intact - decoder loses sync |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.117 | 0.000 | 37 ms | 37 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 37 ms | 37 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.124 | 0.000 | 33 ms | 33 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.126 | 0.000 | 28 ms | 28 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 35 ms | 35 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 35 ms | 35 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 36 ms | 36 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.165 | 0.000 | 37 ms | 37 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.127 | 0.000 | 46 ms | 46 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.126 | 0.000 | 38 ms | 38 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 38 ms | 38 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 37 ms | 37 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 36 ms | 36 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.118 | 0.000 | 37 ms | 37 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.114 | 0.000 | 37 ms | 37 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 13 ms | 13 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.221 | 0.000 | 9 ms | 9 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.171 | 0.000 | 14 ms | 14 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.133 | 0.000 | 22 ms | 22 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.142 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.120 | 0.000 | 56 ms | 56 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.133 | 0.000 | 72 ms | 72 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.126 | 0.000 | 82 ms | 82 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.120 | 0.000 | 37 ms | 37 ms |  |

#### `ss` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.056 | 0.000 | 55 ms | 55 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 55 ms | 55 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.108 | 0.000 | 55 ms | 55 ms |  |
| †blur_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.279 | 0.000 | 54 ms | 54 ms | signal intact - decoder loses sync |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.041 | 0.000 | 54 ms | 54 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 54 ms | 54 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.038 | 0.000 | 48 ms | 48 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.036 | 0.000 | 43 ms | 43 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 52 ms | 52 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 51 ms | 51 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 52 ms | 52 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 52 ms | 52 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 53 ms | 53 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 54 ms | 54 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.105 | 0.000 | 54 ms | 54 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.062 | 0.000 | 54 ms | 54 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.052 | 0.000 | 54 ms | 54 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 54 ms | 54 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.041 | 0.000 | 54 ms | 54 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 54 ms | 54 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.046 | 0.000 | 55 ms | 55 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 55 ms | 55 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 55 ms | 55 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 19 ms | 19 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.163 | 0.000 | 14 ms | 14 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.093 | 0.000 | 20 ms | 20 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.061 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.076 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 43 ms | 43 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 85 ms | 85 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 102 ms | 102 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.047 | 0.000 | 119 ms | 119 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 59 ms | 59 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 55 ms | 55 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 53 ms | 53 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.043 | 0.000 | 53 ms | 53 ms |  |

#### `ss_id` · file 1282×1110 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 192 ms | 192 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 174 ms | 174 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 184 ms | 184 ms |  |
| †blur_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.216 | 0.000 | 177 ms | 177 ms |  |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 175 ms | 175 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 185 ms | 185 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 173 ms | 173 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.002 | 0.000 | 150 ms | 150 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 183 ms | 183 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 176 ms | 176 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 189 ms | 189 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 175 ms | 175 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 183 ms | 183 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 177 ms | 177 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 187 ms | 187 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.093 | 0.000 | 180 ms | 180 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.013 | 0.000 | 178 ms | 178 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 178 ms | 178 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 183 ms | 183 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 178 ms | 178 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 181 ms | 181 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 183 ms | 183 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 180 ms | 180 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.002 | 0.000 | 176 ms | 176 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 178 ms | 178 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 184 ms | 184 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 60 ms | 60 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 103 ms | 103 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.105 | 0.000 | 42 ms | 42 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.031 | 0.000 | 65 ms | 65 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.011 | 0.000 | 96 ms | 96 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.022 | 0.000 | 94 ms | 94 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 150 ms | 150 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 294 ms | 294 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 370 ms | 370 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.005 | 0.000 | 426 ms | 426 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 194 ms | 194 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 182 ms | 182 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 181 ms | 181 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 181 ms | 181 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 186 ms | 186 ms |  |

#### `ss_id` · file 493×356 · α=12 · payload `wmid` · PSNR 32.9 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.049 | 0.000 | 20 ms | 20 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.058 | 0.000 | 21 ms | 21 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.102 | 0.000 | 21 ms | 21 ms |  |
| †blur_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.269 | 0.089 | 21 ms | 21 ms | signal degraded |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.060 | 0.000 | 20 ms | 20 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 20 ms | 20 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.056 | 0.000 | 17 ms | 17 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.060 | 0.000 | 15 ms | 15 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 21 ms | 21 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 19 ms | 19 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 21 ms | 21 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 21 ms | 21 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.062 | 0.000 | 20 ms | 20 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.048 | 0.000 | 21 ms | 21 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.165 | 0.000 | 21 ms | 21 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.058 | 0.000 | 21 ms | 21 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.058 | 0.000 | 21 ms | 21 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 21 ms | 21 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.051 | 0.000 | 21 ms | 21 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 21 ms | 21 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.055 | 0.000 | 20 ms | 20 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.049 | 0.000 | 21 ms | 21 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 21 ms | 21 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 9 ms | 9 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 11 ms | 11 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 6 ms | 6 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.087 | 0.000 | 8 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.064 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.074 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.064 | 0.000 | 17 ms | 17 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.059 | 0.000 | 32 ms | 32 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.063 | 0.000 | 41 ms | 41 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.059 | 0.000 | 47 ms | 47 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.054 | 0.000 | 20 ms | 20 ms |  |

#### `ss_id` · file 512×480 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.006 | 0.000 | 30 ms | 30 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 30 ms | 30 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms |  |
| †blur_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.118 | 0.000 | 29 ms | 29 ms |  |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 29 ms | 29 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 26 ms | 26 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.004 | 0.000 | 23 ms | 23 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 28 ms | 28 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 30 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.102 | 0.000 | 29 ms | 29 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.008 | 0.000 | 29 ms | 29 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.005 | 0.000 | 30 ms | 30 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 31 ms | 31 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 30 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 30 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.003 | 0.000 | 30 ms | 30 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 10 ms | 10 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 16 ms | 16 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.050 | 0.000 | 8 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.021 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.008 | 0.000 | 17 ms | 17 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.018 | 0.000 | 17 ms | 17 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 24 ms | 24 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.006 | 0.000 | 47 ms | 47 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 58 ms | 58 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.007 | 0.000 | 67 ms | 67 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 30 ms | 30 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 29 ms | 29 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.004 | 0.000 | 30 ms | 30 ms |  |

#### `ss_id` · file 512×512 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 31 ms | 31 ms |  |
| blur_0.5 | 2 | 100.0% [34%–100%] | 0.0% | 0.031 | 0.000 | 39 ms | 46 ms |  |
| blur_1.0 | 2 | 100.0% [34%–100%] | 0.0% | 0.074 | 0.000 | 31 ms | 32 ms |  |
| †blur_1.5 | 2 | 50.0% [9%–91%] | 0.0% | 0.185 | 0.009 | 32 ms | 32 ms | signal intact - decoder loses sync |
| brightness_+25 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 31 ms |  |
| contrast_0.8 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 32 ms | 32 ms |  |
| crop_top_64 | 2 | 100.0% [34%–100%] | 0.0% | 0.021 | 0.000 | 28 ms | 28 ms |  |
| †crop_topleft_64 | 2 | 0.0% [0%–66%] | 0.0% | 0.021 | 0.000 | 25 ms | 25 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †crop_unaligned_15 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 30 ms | 30 ms | no oracle geometry |
| †crop_unaligned_3 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †crop_unaligned_7 | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| †flip_horizontal | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| gamma_1.3 | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 32 ms | 33 ms |  |
| identity | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 33 ms | 33 ms |  |
| †jpeg_30 | 2 | 100.0% [34%–100%] | 0.0% | 0.093 | 0.000 | 31 ms | 31 ms |  |
| jpeg_50 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 32 ms | 32 ms |  |
| jpeg_60 | 2 | 100.0% [34%–100%] | 0.0% | 0.030 | 0.000 | 31 ms | 32 ms |  |
| jpeg_75 | 2 | 100.0% [34%–100%] | 0.0% | 0.027 | 0.000 | 32 ms | 32 ms |  |
| jpeg_85 | 2 | 100.0% [34%–100%] | 0.0% | 0.024 | 0.000 | 32 ms | 32 ms |  |
| jpeg_95 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 32 ms | 32 ms |  |
| †noise_10 | 2 | 100.0% [34%–100%] | 0.0% | 0.028 | 0.000 | 32 ms | 32 ms |  |
| noise_2 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 31 ms | 32 ms |  |
| noise_5 | 2 | 100.0% [34%–100%] | 0.0% | 0.025 | 0.000 | 32 ms | 32 ms |  |
| †perspective_light | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| †perspective_medium | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| †pipeline_heavy_repost | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 11 ms | 11 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 17 ms | 17 ms | no oracle geometry |
| †resize_0.5 | 2 | 0.0% [0%–66%] | 0.0% | 0.119 | 0.000 | 8 ms | 8 ms | signal intact - decoder loses sync |
| †resize_0.62 | 2 | 0.0% [0%–66%] | 0.0% | 0.064 | 0.000 | 12 ms | 12 ms | signal intact - decoder loses sync |
| †resize_0.75 | 2 | 0.0% [0%–66%] | 0.0% | 0.039 | 0.000 | 18 ms | 18 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 2 | 0.0% [0%–66%] | 0.0% | 0.046 | 0.000 | 18 ms | 18 ms | signal intact - decoder loses sync |
| †resize_0.9 | 2 | 0.0% [0%–66%] | 0.0% | 0.034 | 0.000 | 25 ms | 26 ms | signal intact - decoder loses sync |
| †resize_1.25 | 2 | 0.0% [0%–66%] | 0.0% | 0.030 | 0.000 | 50 ms | 50 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 2 | 0.0% [0%–66%] | 0.0% | 0.034 | 0.000 | 62 ms | 62 ms | signal intact - decoder loses sync |
| †resize_1.5 | 2 | 0.0% [0%–66%] | 0.0% | 0.031 | 0.000 | 71 ms | 71 ms | signal intact - decoder loses sync |
| †rotate_1deg | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 31 ms | no oracle geometry |
| †rotate_2deg | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 32 ms | 32 ms | no oracle geometry |
| †rotate_3deg | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 32 ms | 33 ms | no oracle geometry |
| †rotate_5deg | 2 | 0.0% [0%–66%] | 0.0% | n/a | n/a | 31 ms | 32 ms | no oracle geometry |
| webp_80 | 2 | 100.0% [34%–100%] | 0.0% | 0.026 | 0.000 | 31 ms | 31 ms |  |

#### `ss_id` · file 640×480 · α=12 · payload `wmid` · PSNR 32.6 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 37 ms | 37 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.126 | 0.000 | 37 ms | 37 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.178 | 0.000 | 37 ms | 37 ms |  |
| †blur_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.292 | 0.000 | 37 ms | 37 ms |  |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.117 | 0.000 | 37 ms | 37 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 37 ms | 37 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.124 | 0.000 | 32 ms | 32 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.126 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 34 ms | 34 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 36 ms | 36 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 38 ms | 38 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 36 ms | 36 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.165 | 0.000 | 37 ms | 37 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.127 | 0.000 | 38 ms | 38 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.126 | 0.000 | 41 ms | 41 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.121 | 0.000 | 37 ms | 37 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 38 ms | 38 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.116 | 0.000 | 36 ms | 36 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.118 | 0.000 | 38 ms | 38 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.114 | 0.000 | 37 ms | 37 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.115 | 0.000 | 37 ms | 37 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 13 ms | 13 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 20 ms | 20 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.221 | 0.000 | 10 ms | 10 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.171 | 0.000 | 14 ms | 14 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.133 | 0.000 | 22 ms | 22 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.142 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.130 | 0.000 | 29 ms | 29 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.120 | 0.000 | 57 ms | 57 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.133 | 0.000 | 73 ms | 73 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.126 | 0.000 | 82 ms | 82 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 40 ms | 40 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 38 ms | 38 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 37 ms | 37 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.120 | 0.000 | 37 ms | 37 ms |  |

#### `ss_id` · file 752×600 · α=12 · payload `wmid` · PSNR 32.7 dB

| attack | n | detect [95% CI] | misdecode | BER raw | BER comb | p50 | p95 | reading |
|---|---|---|---|---|---|---|---|---|
| avif_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.056 | 0.000 | 55 ms | 55 ms |  |
| blur_0.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.050 | 0.000 | 55 ms | 55 ms |  |
| blur_1.0 | 1 | 100.0% [21%–100%] | 0.0% | 0.108 | 0.000 | 55 ms | 55 ms |  |
| †blur_1.5 | 1 | 100.0% [21%–100%] | 0.0% | 0.279 | 0.000 | 55 ms | 55 ms |  |
| brightness_+25 | 1 | 100.0% [21%–100%] | 0.0% | 0.041 | 0.000 | 54 ms | 54 ms |  |
| contrast_0.8 | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 54 ms | 54 ms |  |
| crop_top_64 | 1 | 100.0% [21%–100%] | 0.0% | 0.038 | 0.000 | 47 ms | 47 ms |  |
| †crop_topleft_64 | 1 | 0.0% [0%–79%] | 0.0% | 0.036 | 0.000 | 44 ms | 44 ms | signal intact - decoder loses sync |
| †crop_unaligned_1 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 52 ms | 52 ms | no oracle geometry |
| †crop_unaligned_15 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 51 ms | 51 ms | no oracle geometry |
| †crop_unaligned_3 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| †crop_unaligned_7 | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 52 ms | 52 ms | no oracle geometry |
| †flip_horizontal | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| gamma_1.3 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 53 ms | 53 ms |  |
| identity | 1 | 100.0% [21%–100%] | 0.0% | 0.039 | 0.000 | 54 ms | 54 ms |  |
| †jpeg_30 | 1 | 100.0% [21%–100%] | 0.0% | 0.105 | 0.000 | 55 ms | 55 ms |  |
| jpeg_50 | 1 | 100.0% [21%–100%] | 0.0% | 0.062 | 0.000 | 54 ms | 54 ms |  |
| jpeg_60 | 1 | 100.0% [21%–100%] | 0.0% | 0.052 | 0.000 | 54 ms | 54 ms |  |
| jpeg_75 | 1 | 100.0% [21%–100%] | 0.0% | 0.044 | 0.000 | 53 ms | 53 ms |  |
| jpeg_85 | 1 | 100.0% [21%–100%] | 0.0% | 0.041 | 0.000 | 54 ms | 54 ms |  |
| jpeg_95 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 54 ms | 54 ms |  |
| †noise_10 | 1 | 100.0% [21%–100%] | 0.0% | 0.046 | 0.000 | 55 ms | 55 ms |  |
| noise_2 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 55 ms | 55 ms |  |
| noise_5 | 1 | 100.0% [21%–100%] | 0.0% | 0.040 | 0.000 | 55 ms | 55 ms |  |
| †perspective_light | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| †perspective_medium | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| †pipeline_heavy_repost | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 19 ms | 19 ms | no oracle geometry |
| †pipeline_resize_jpeg_crop | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 30 ms | 30 ms | no oracle geometry |
| †resize_0.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.163 | 0.000 | 14 ms | 14 ms | signal intact - decoder loses sync |
| †resize_0.62 | 1 | 0.0% [0%–79%] | 0.0% | 0.093 | 0.000 | 21 ms | 21 ms | signal intact - decoder loses sync |
| †resize_0.75 | 1 | 0.0% [0%–79%] | 0.0% | 0.061 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †resize_0.75_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.076 | 0.000 | 30 ms | 30 ms | signal intact - decoder loses sync |
| †resize_0.9 | 1 | 0.0% [0%–79%] | 0.0% | 0.053 | 0.000 | 43 ms | 43 ms | signal intact - decoder loses sync |
| †resize_1.25 | 1 | 0.0% [0%–79%] | 0.0% | 0.048 | 0.000 | 84 ms | 84 ms | signal intact - decoder loses sync |
| †resize_1.4_jpeg85 | 1 | 0.0% [0%–79%] | 0.0% | 0.054 | 0.000 | 103 ms | 103 ms | signal intact - decoder loses sync |
| †resize_1.5 | 1 | 0.0% [0%–79%] | 0.0% | 0.047 | 0.000 | 122 ms | 122 ms | signal intact - decoder loses sync |
| †rotate_1deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 55 ms | 55 ms | no oracle geometry |
| †rotate_2deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| †rotate_3deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 53 ms | 53 ms | no oracle geometry |
| †rotate_5deg | 1 | 0.0% [0%–79%] | 0.0% | n/a | n/a | 54 ms | 54 ms | no oracle geometry |
| webp_80 | 1 | 100.0% [21%–100%] | 0.0% | 0.043 | 0.000 | 54 ms | 54 ms |  |

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
| decode:ss | 493×356 | 1 | 21 ms | 21 ms | 21 ms | 117 ms |  |
| decode:ss | 512×480 | 1 | 30 ms | 30 ms | 30 ms | 122 ms |  |
| decode:ss | 512×512 | 2 | 32 ms | 32 ms | 32 ms | 121 ms |  |
| decode:ss | 640×480 | 1 | 36 ms | 36 ms | 36 ms | 119 ms |  |
| decode:ss | 752×600 | 1 | 54 ms | 54 ms | 54 ms | 119 ms |  |
| decode:ss | 1282×1110 | 1 | 183 ms | 183 ms | 183 ms | 129 ms |  |
| decode:ss_id | 493×356 | 1 | 21 ms | 21 ms | 21 ms | 120 ms |  |
| decode:ss_id | 512×480 | 1 | 30 ms | 30 ms | 30 ms | 121 ms |  |
| decode:ss_id | 512×512 | 2 | 33 ms | 33 ms | 33 ms | 124 ms |  |
| decode:ss_id | 640×480 | 1 | 36 ms | 36 ms | 36 ms | 118 ms |  |
| decode:ss_id | 752×600 | 1 | 54 ms | 54 ms | 54 ms | 120 ms |  |
| decode:ss_id | 1282×1110 | 1 | 187 ms | 187 ms | 187 ms | 131 ms |  |
| embed:ss | 493×356 | 1 | 37 ms | 37 ms | 37 ms | 209 ms |  |
| embed:ss | 512×480 | 1 | 53 ms | 53 ms | 53 ms | 217 ms |  |
| embed:ss | 512×512 | 2 | 55 ms | 56 ms | 56 ms | 211 ms |  |
| embed:ss | 640×480 | 1 | 64 ms | 64 ms | 64 ms | 209 ms |  |
| embed:ss | 752×600 | 1 | 95 ms | 95 ms | 95 ms | 210 ms |  |
| embed:ss | 1282×1110 | 1 | 466 ms | 466 ms | 466 ms | 328 ms |  |
