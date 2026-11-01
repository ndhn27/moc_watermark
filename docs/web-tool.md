# Web tool

[← Back to the README](../README.md)

Open `web/index.html` in a browser (or serve it as a static page, see
below). Drag in **one or more** images, tune text / opacity / density / font
size / angle / color, and:

- **Download this image** — the currently-selected image only.
- **Download all as .zip** — watermarks every loaded image with the same
  settings and bundles them into a single `.zip`, with a progress bar while
  it works. The zip is built entirely client-side (no library, no upload).

Switch between loaded images using the thumbnail strip above the preview;
each keeps its own original resolution on export. Video isn't supported in
the browser tool — use the CLI for that.

## Run it locally

```bash
# no build step — just open the file (fully client-side, nothing is uploaded)
open web/index.html        # macOS
xdg-open web/index.html    # Linux
```

## Full pipeline (optional server mode)

The page above draws a plain regular grid in your browser — it deliberately
has no jitter, blend modes, invisible marks, metadata or C2PA, because those
live in Python. To get them in the page too, run the bundled server and open
the page *from it*:

```bash
python3 cli/serve.py            # http://127.0.0.1:8765/  — the page + the API, this machine only
```

The page detects the server and shows a **Full pipeline (server)** switch,
off by default. Turn it on and the download buttons render on the server
with the *same code as the CLI and the Python API* (identical pixels — see
`tests/test_frontends_parity.py`); the extra controls (blend, ink, invisible
mark, key, author, adaptive placement, C2PA…) are built from the server's
`/api/schema`, so an option added in `cli/wmapp/options.py` appears here
without touching the page. The page says plainly when this is on that images
are sent to the server (and not stored); switch it off and everything is
back in the browser. The preview stays the local approximation — it can't
show jitter or invisible marks — so use **Render preview on server** to see
the real result, or just download.

The server is standard-library only and meant for your own machine. It binds
`127.0.0.1`; requests can't name server-side paths (font, certificate,
preview output, ledger — `--id` records into the server's own ledger,
`serve.py --ledger PATH`, and `/api/extract` returns the record without the
key or settings); upload size, pixel count, grid density and text length are
capped (`wmapp.SERVER_LIMITS`); the `Host` header must be a loopback name
(DNS-rebinding); and there is no CORS unless you pass `--cors-origin ORIGIN`
for one specific origin. Images only — video stays a CLI feature.

## Host it (e.g. GitHub Pages)

Since it's a static, single HTML file, you can publish it directly with GitHub
Pages: **Settings → Pages → Deploy from a branch**, and point it at the `web/`
folder (or copy `index.html` to the repo root / a `docs/` folder, depending on
how you want Pages configured).
