# Architecture & Python API

[← Back to the README](../README.md)

The CLI, the web page's full-pipeline mode and Python callers all sit on one
application layer, `cli/wmapp/`, so a feature or a default exists in exactly one place:

```
   wmcore   image primitives: grid, adaptive placement, blend, LSB / spread-spectrum marks,
      ▲     the resize-recovery search, metadata
   wmapp    what the tool DOES: one option schema, validated requests, the watermark pipeline,
      ▲     batch fan-out, read-back, structured results and notes, resource limits
      │
   ┌──┴───────────────────────┬──────────────────────────────┬────────────────────────┐
   watermark.py               serve.py (stdlib HTTP)         your Python code
   extract_invisible.py       GET /api/schema                import wmapp
   c2pa_verify.py             POST /api/watermark|extract|verify
   wm_ledger.py
   argv → spec → call → print JSON/bytes → spec → call → JSON/bytes
```

A front-end parses its own input format into a `WatermarkSpec` / `ExtractSpec`,
calls one function, and renders the result its own way — none re-implements
behaviour, so they can't drift. `tests/test_frontends_parity.py` proves it:
the same job through the CLI (a real subprocess), the Python API and HTTP
gives identical pixels, and the hidden mark reads back identically through each.

```python
import sys; sys.path.insert(0, "cli")          # not pip-installable (yet): cli/ is the import root
import wmapp

r = wmapp.watermark("in.jpg", "out.png", text="@me", blend="multiply",
                    invisible=True, invisible_mode="spread")     # spread mark, key generated for you
r.ss_key, r.c2pa, r.seconds                      # the key to read it back, "off"/"signed"/"failed", timing
[n.message for n in r.notes]                     # everything the CLI would have printed - a library doesn't print
wmapp.extract("out.png", mode="spread", ss_key=r.ss_key).text   # "@me"
wmapp.extract("small.png", mode="spread", ss_key=r.ss_key, rescale=True)   # after a resize: search for the scale (see --rescale)

r = wmapp.watermark("in.jpg", "out.jpg", text="@me", stamp_id=True, invisible=True, invisible_mode="spread")
r.wm_id, r.id_layers                             # a short ID, and which layers carry it (see "Watermark ID & ledger")
wmapp.extract("suspect.jpg").record              # no key needed: the ledger's keys are tried; the ID's record comes back

wmapp.watermark_batch("photos/", "marked/", wmapp.WatermarkSpec(text="@me", seed=7), workers=4)
spec = wmapp.WatermarkSpec.from_mapping({"text": "@me", "opacity": 120})   # from JSON / a config file
wmapp.schema()                                   # every option: type, default, range, help, group
```

`watermark_batch` runs worker processes: on macOS/Windows (the `spawn` start method) call it from
under `if __name__ == "__main__":`, as the CLI scripts do.

Errors are `wmapp.SpecError` (a `ValueError`: bad value, unknown option, contradictory flags),
`UnavailableError` (C2PA packages missing) and `LimitError` (a configured `Limits` exceeded —
the CLI and Python API default to none; the HTTP server applies `SERVER_LIMITS`).

**Adding or changing an option is one edit** — an entry in `cli/wmapp/options.py`. From that
list are generated the CLI flag (and its `--help` text), the `WatermarkSpec` field with its
default and range check, and the entry in `/api/schema` that the web page renders. Options
that name a path on the machine running the code (`local=True`: font, certificate, preview
output) exist for the CLI/Python API and are refused over HTTP.

What this does *not* unify: the static, client-side web mode is still its own small canvas
implementation (different font, no jitter) and is an approximation of the real output, not a
copy of it; and video is CLI/Python only.

## Project structure

```
.
├── cli/
│   ├── wmcore/                 # Image primitives: grid, adaptive placement, blend, invisible marks (LSB, spread-spectrum, resize-recovery search, mirrored-copy search in orient.py) + their read-back, metadata, watermark-ID format (wmid.py)
│   ├── wmapp/                  # Application layer shared by every front-end (see "Architecture")
│   │   ├── options.py          #   THE option list -> CLI flags, WatermarkSpec/ExtractSpec, /api/schema
│   │   ├── pipeline.py         #   prepare(), watermark(), watermark_file(), watermark_batch()
│   │   ├── extraction.py       #   extract() (ID- and ledger-aware), verify(), capabilities()
│   │   ├── ledger.py           #   the SQLite ledger behind --id: ID -> file, hashes, key, layers, settings
│   │   └── limits.py, events.py, errors.py
│   ├── watermark.py            # CLI shell over wmapp: images, batch, video
│   ├── extract_invisible.py    # CLI shell: reads back either invisible-mark scheme (lsb or spread); with --id marks, the ID + its ledger record
│   ├── wm_ledger.py            # CLI shell: look up / list / find IDs in the ledger
│   ├── c2pa_verify.py          # CLI shell: reads back a --c2pa manifest
│   ├── serve.py                # HTTP shell (stdlib): serves web/ and /api/{schema,watermark,extract,verify}
│   ├── video.py                # Video pipeline: parallel frame workers, ffmpeg mux/encode, per-frame invisible mark
│   └── c2pa_provenance.py      # C2PA (Content Credentials): dev-cert gen/reuse, sign_file(), read_manifest()
├── tests/                      # pytest: primitives, the application layer, CLI shells, HTTP adapter, cross-front-end parity, bench/
│   └── js/                     # Node tests for the web page's server mode (client module; page boot in jsdom)
├── docs/                       # the full documentation (the README is the short version)
│   ├── cli.md, web-tool.md     #   usage: every CLI flag; the browser tool and its optional server mode
│   ├── visible-mark.md, invisible-marks.md, id-and-ledger.md, c2pa.md, video.md
│   ├── threat-model.md, known-limitations.md
│   ├── architecture.md, testing.md, benchmarks.md
│   └── img/                    # demo images used by the README
├── .github/workflows/tests.yml # CI: pytest + the Node tests on every push / pull request
├── bench/                      # measurement framework: detection rate / BER / FPR / runtime under attack (see bench/README.md)
├── web/
│   └── index.html              # Browser tool: multi-image batch, zip export; client-side by default, full pipeline via serve.py
├── requirements.txt            # version ranges
├── requirements-lock.txt       # exact versions of the tested environment (Python >= 3.12)
├── requirements-dev.txt        # requirements.txt + pytest (+ tifffile, imagecodecs: only for the bench TIFF probes)
├── pyproject.toml              # metadata + pytest config; dependencies are read from requirements.txt
├── LICENSE                     # PolyForm Noncommercial 1.0.0 + Required Notice line
└── README.md
```
