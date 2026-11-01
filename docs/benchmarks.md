# Benchmarks

[← Back to the README](../README.md)

`pytest` says whether a case passes; it can't say *how often* a mark
survives, how much signal is left when it doesn't, how often a decoder
reports a payload that isn't there, or how long the rescale search takes.
`bench/` measures those:

```bash
python3 bench/run_benchmark.py --suite quick       # ~1-2 min, one core
python3 bench/run_benchmark.py --suite standard    # the real measurement
python3 bench/run_benchmark.py --suite standard --images ~/photos   # on real photos
python3 bench/run_benchmark.py --suite quick --baseline bench/baselines/quick.json  # CI gate
python3 bench/run_benchmark.py --suite quick --decoders ss,ss_id --payloads wmid    # text vs ID-aware decoder, same images
```

There is no baseline file in the repo yet: create one first with
`python3 bench/run_benchmark.py --suite quick --save-baseline bench/baselines/quick.json`, then compare later runs
against it with `--baseline` (details in [bench/README.md](../bench/README.md)).

Each run writes `report.md` (detection rate with 95% intervals, raw and
combined BER against oracle alignment, false-positive rate on unmarked images
and on wrong keys, embed/decode/rescale runtime p50/p95) plus raw
per-trial records. See [bench/README.md](../bench/README.md) for definitions,
how to read a report, and how to extend it.
