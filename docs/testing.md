# Tests

[← Back to the README](../README.md)

```bash
pip install -r requirements-dev.txt
pytest tests/
```

The video tests need an `ffmpeg` binary on PATH: without one, 4 of them fail (the tool itself degrades with a
`ffmpeg_missing` note, but those tests expect the full pipeline).

GitHub Actions runs the same thing on every push and pull request (`.github/workflows/tests.yml`): the exact
environment in `requirements-lock.txt` on Python 3.12 (must pass), plus Python 3.10, 3.11 and 3.13 with the version
ranges in `requirements.txt`. Those three are informational: they do not fail the run, because 3.10 and 3.11 have never
been tried and 3.13 only partly. Once one of them is green, make it required.

Covers the blend-mode math (`wmcore.blend_arrays`, all three modes), the
content-adaptive placement math (`wmcore.build_ink_map`, sensitivity-map
shape/range guarantees), both invisible-mark embed/extract round trips
(`lsb` and `spread`), and C2PA sign/read round trips including the
dev-cert generate-then-reuse behavior and the self-signed
`signingCredential.untrusted` expectation - these are the places most
likely to silently regress since none has an obvious "it crashed" failure
mode (a wrong blend, a broken payload, or a manifest missing a field all
just *look* fine at a glance). The C2PA tests are skipped automatically if
`c2pa-python`/`cryptography` aren't installed.

The application layer is tested three ways: directly through the Python API
(`test_wmapp.py`: schema consistency, validation, notes, limits — including that
the tile-count estimate equals what `wmcore` really draws — batch, video,
extract, backward compatibility), through each shell (`test_cli_shell.py` for
argparse/exit codes, `test_serve.py` for the HTTP API and what it refuses), and
across them (`test_frontends_parity.py`: identical pixels and identical
read-back from CLI, Python and HTTP — for `--id` stamps too). The ID format is
`test_wmid.py`, the ledger `test_ledger.py` (including several processes writing
at once), and `--id` end to end — every layer, batch, video, `extract` with and
without a key, a resized or recompressed copy, a junk LSB decode — `test_id_ledger.py`; mirrored
copies (every orientation, an odd image size, a JPEG re-save, the ordering rule that stops junk text
beating a mirrored ID, and `extract`'s wording) `test_orient.py`; the per-layer report of `extract` (every layer's own outcome, why a layer was not
checked, the disagreement warning, the plain-decode shortcut, video) `test_extract_layers.py`; crop re-alignment (grid filter == DCT correlations, off-grid / left-right / mirrored
crops, JPEG, mark-free images, the width limit, `extract`, video, the mirroring label with several ledger keys, the pre-screen, crop + resize) `test_resync.py`.
That file's given-key test (`extract --ss-key` on a crop, with and without `--no-resync`) asserts "no ID read, the crop search did not run, and
nothing found or the report says `--rescale`" rather than "nothing found", because the plain decoders can return junk (previous bullet of
*Known limitations*); six recorded crops that make the LSB layer return junk run it every time, not one run in fifteen.
transparent PNGs (every embedder keeps alpha: alpha 0 / partial / 255 / a ramp / a palette image) and phone-photo orientation (all 8 EXIF values, a JPEG with `--author`/`--id`, orientation plus alpha) `test_alpha_orientation.py`; output formats beyond PNG (transparent input to JPEG/BMP is laid on white before stamping, alpha kept exactly in WebP/TIFF, which hidden marks each format keeps and whether the LSB warning is true, orientation in WebP/TIFF, every input/output extension pair, formats without a metadata writer, the Pillow RGBA-TIFF orientation bug as a strict xfail) `test_output_formats.py`.
`conftest.py` points the default ledger at a per-test path, so no test touches a
real `~/.watermark-tool/ledger.sqlite3`. `test_web_client.py` runs the JavaScript
tests in `tests/js/` against a real server; it needs Node ≥ 20 and is skipped
without it (run `npm install` in `tests/js/` to also enable the jsdom test that
boots the whole page).
