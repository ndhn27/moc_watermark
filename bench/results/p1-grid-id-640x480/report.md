# --grid-id vs the hidden spread mark (real pipeline, 640x480 synthetic pink,gradnoise, n=16 images per cell)

| config | attack | correct / n | rate [95% Wilson] | wrong | budget hit |
|---|---|---|---|---|---|
| A legacy payload, short grid text | identity | 16/16 | 100% [81%, 100%] | 0 | 0 |
| A legacy payload, short grid text | jpeg_q60 | 16/16 | 100% [81%, 100%] | 0 | 0 |
| A legacy payload, short grid text | jpeg_q40 | 16/16 | 100% [81%, 100%] | 0 | 0 |
| A legacy payload, short grid text | resize_0.75 (+rescale) | 16/16 | 100% [81%, 100%] | 0 | 0 |
| B --id, short grid text | identity | 16/16 | 100% [81%, 100%] | 0 | 0 |
| B --id, short grid text | jpeg_q60 | 16/16 | 100% [81%, 100%] | 0 | 0 |
| B --id, short grid text | jpeg_q40 | 16/16 | 100% [81%, 100%] | 0 | 0 |
| B --id, short grid text | resize_0.75 (+rescale) | 16/16 | 100% [81%, 100%] | 0 | 0 |
| C --id --grid-id (long grid text) | identity | 16/16 | 100% [81%, 100%] | 0 | 0 |
| C --id --grid-id (long grid text) | jpeg_q60 | 16/16 | 100% [81%, 100%] | 0 | 0 |
| C --id --grid-id (long grid text) | jpeg_q40 | 16/16 | 100% [81%, 100%] | 0 | 0 |
| C --id --grid-id (long grid text) | resize_0.75 (+rescale) | 16/16 | 100% [81%, 100%] | 0 | 0 |
| D legacy payload, long grid text | identity | 16/16 | 100% [81%, 100%] | 0 | 0 |
| D legacy payload, long grid text | jpeg_q60 | 16/16 | 100% [81%, 100%] | 0 | 0 |
| D legacy payload, long grid text | jpeg_q40 | 16/16 | 100% [81%, 100%] | 0 | 0 |
| D legacy payload, long grid text | resize_0.75 (+rescale) | 16/16 | 100% [81%, 100%] | 0 | 0 |
