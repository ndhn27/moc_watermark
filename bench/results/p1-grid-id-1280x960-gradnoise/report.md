# --grid-id vs the hidden spread mark (real pipeline, 1280x960 synthetic gradnoise, n=10 images per cell)

| config | attack | correct / n | rate [95% Wilson] | wrong | budget hit |
|---|---|---|---|---|---|
| A legacy payload, short grid text | resize_0.75 (+rescale) | 3/10 | 30% [11%, 60%] | 0 | 0 |
| B --id, short grid text | resize_0.75 (+rescale) | 3/10 | 30% [11%, 60%] | 0 | 0 |
| C --id --grid-id (long grid text) | resize_0.75 (+rescale) | 3/10 | 30% [11%, 60%] | 0 | 0 |
| D legacy payload, long grid text | resize_0.75 (+rescale) | 0/10 | 0% [0%, 28%] | 0 | 0 |
