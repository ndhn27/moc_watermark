# Watermark ID & ledger (`--id`)

[← Back to the README](../README.md)

Every layer of this tool dies in a different way (recompression, a resize, a crop, a re-encode, a
stripped header), which is why they are stacked. Until `--id`, each layer carried whatever text you
gave it, and reading the `spread` mark back needed the exact `--ss-key` — which nothing stored (the
CLI printed it once, "SAVE THIS"). `--id` fixes both:

- **One short ID per output file** — 10 characters (Crockford base32: 8 random characters = 40 bits,
  plus 2 check characters), shown as `K3M9-QXR2-T4`. The same ID goes into every layer that can carry
  it: the hidden mark (in place of the long text; `--invisible`), the image metadata (PNG text chunk
  `WatermarkID`, JPEG EXIF `ImageUniqueID`), the C2PA manifest (schema.org `identifier`, `wmid:…`;
  `--c2pa`), and — only if you ask, `--grid-id` — the visible grid.
- **A ledger** — one SQLite file, `~/.watermark-tool/ledger.sqlite3` (or `--ledger PATH`, or
  `$WATERMARK_TOOL_LEDGER`), created `0600` because it stores spread-spectrum keys. One row per ID: the
  input and output file names, the SHA-256 of the input and of the **finished** output (after metadata
  and C2PA), the hidden-mark scheme, key and strength, which layers carry the ID, and the settings. The
  row is written *before* the file is stamped (`pending`) and completed afterwards, so a crash can't
  release an image whose ID the ledger has never heard of.
- **`extract` needs nothing but the file.** With no `--ss-key` it tries every key the ledger recorded
  (newest first) and accepts only a well-formed ID. It then reports the ledger record and whether the
  file is **byte-identical** to the recorded output. The `spread` layer is read by an ID-aware decoder
  first (below), then by the text decoder, so text payloads read back exactly as before.
- **`extract` checks every layer, and can tell you what each one found.** In `auto` mode it reads the
  LSB mark, the spread-spectrum mark, the metadata and the C2PA manifest *each on its own*, instead of
  stopping at the first that gives an ID. The headline answer (`found`, `text`, `scheme`, the lines it
  prints) is picked exactly as before — LSB, else spread-spectrum, else metadata, else C2PA — so nothing
  that read the result needs to change. What is new is `res.layers`: one entry per layer, never folded
  into a single number, with a status of `found` (a real watermark ID), `text` (a payload that isn't an
  ID), `none` (checked, nothing readable), `inconclusive` (the resize search ran out of time — not a
  confirmed absence) or `skipped` (not checked, with the reason: a `--mode`, no key to try, C2PA support
  not installed). On a reposted copy that is what tells you *which layers survived*: typically the
  metadata is gone and the spread-spectrum mark is what's left. Add `--layers` (Python: `layers=True`;
  HTTP: `{"layers": true}`) to print it; the data is in the Python/JSON result either way. **If two
  layers read two different IDs** a warning is printed regardless of `--layers` — a file stamped once
  carries the same ID everywhere, so a disagreement means it was stamped again, or one layer misread — and
  the headline is still just the first match in the order above, not necessarily the original stamp.
  One deliberate shortcut: when the LSB layer already read a real ID, `--rescale`'s resize search is not
  run for the spread-spectrum layer — a resize destroys an LSB mark, so that search could only burn its
  budget on a "not found"; the layer's note says so. The flip search still runs (a top-bottom flip does
  *not* break an LSB mark). Checking every layer costs real time when LSB reads first: a 6-megapixel
  image that used to return in 0.4 s now takes about 4 s (a 640×480 one, 0.03 s → 0.2 s) — the same as
  an image with no mark at all. Measurements and what was not measured:
  `bench/results/EXTRACT-LAYERS-NOTES.md`.

```bash
python3 cli/watermark.py in.jpg out.jpg --text "@yourhandle" --id --invisible --invisible-mode spread --c2pa
#   Watermark ID: XT55-RS4D-Z0 (carried by: spread, metadata, c2pa); recorded in ~/.watermark-tool/ledger.sqlite3. ...

python3 cli/extract_invisible.py suspect.jpg           # no key: the ledger's keys are tried
#   Watermark ID: XT55-RS4D-Z0
#   (found in the spread-spectrum mark, with a key from the ledger)
#   Ledger: stamped 2026-09-20T21:03:10+00:00 from 'in.jpg' as 'out.jpg' (image).
#   Layers that carry this ID: spread, metadata, c2pa.
#   This file is NOT byte-identical to the recorded output: it was re-encoded or edited after stamping -
#   or it is a different image that carries a copied ID. The ID alone can't tell those apart.

python3 cli/extract_invisible.py reposted.jpg --layers   # a re-upload: metadata stripped, pixels recompressed
#   Watermark ID: XT55-RS4D-Z0
#   (found in the spread-spectrum mark, with a key from the ledger)
#   ...
#   This file, layer by layer (each checked on its own - a hit in one says nothing about the others):
#     LSB mark:             nothing readable
#     spread-spectrum mark: found XT55-RS4D-Z0 (1 of 1 ledger key(s) tried)
#     image metadata:       nothing readable
#     C2PA manifest:        nothing readable

python3 cli/wm_ledger.py show XT55-RS4D-Z0             # everything on record (--secrets adds the key + settings)
python3 cli/wm_ledger.py find suspect.jpg              # is this exact file one we stamped? (by SHA-256)
python3 cli/wm_ledger.py list                          # newest first
```

```python
r = wmapp.watermark("in.jpg", "out.jpg", text="@me", stamp_id=True, invisible=True, invisible_mode="spread")
r.wm_id, r.id_layers                       # "XT55RS4DZ0", ["spread", "metadata"]
res = wmapp.extract("suspect.jpg")         # no key; res.wm_id, res.record, res.exact_match, res.scheme
[(l.layer, l.status) for l in res.layers]  # [("lsb","none"), ("spread","found"), ("metadata","none"), ("c2pa","none")]
```

**Batches** get one ID per file (they share one `--ss-key`, as before, so the ledger lists it once).
`--id-value` names one specific ID and so can't be used with `--batch`; an ID already in the ledger is
refused. **Video** can now also carry the ID in a hidden mark, same as images: add `--invisible
--invisible-mode spread` (see [Video support](video.md#video-support) for what's different about it there
- a higher default `--ss-alpha`, per-segment key rotation, `extract_invisible.py` scanning every
frame). Without that, a video's ID lives only in the visible grid (`--grid-id`) and the C2PA
manifest (`--c2pa`); `--id` on a video with none of the three prints a warning, because then the ID
is recorded in the ledger but written into nothing the file carries.

**What an ID is not.**

- **Not a proof.** Anyone who can read an ID can copy it into a different file — trivially so from
  the metadata or a visible `--grid-id`. The ledger's output hash lets `extract` say "byte-identical to
  what I stamped", but for a re-encoded copy it can't tell "my image, recompressed" from "someone else's
  image carrying my ID". (Storing a perceptual hash in the ledger to compare content is not implemented.)
  The [threat model](threat-model.md) applies unchanged.
- **Not a secret.** The `--ss-key` is still a reproducibility value, not access control: roughly one
  wrong key in four still decodes a text payload, and a bit more often an ID (about 3 in 10 on
  synthetic images, see the next bullet; with `--resync` on, which retries the decode on a few shifted
  block grids, far more often — see "Crop resync"). The ID's check characters are what let `extract` accept a
  decode from a key that isn't the recorded one, and reject the junk other wrong keys produce.
- **Not a robustness upgrade over a short handle.** A shorter payload means more repeats per image, and
  that matters only for *sentence-length* payloads on *small* images: on synthetic 640×480 images a
  10-byte ID, an 11-byte handle and a 99-byte sentence were all detected 16/16 under every gated attack,
  but at 320×240 the 99-byte payload failed even unattacked (12/16) and under a 64 px top crop (0/16)
  while the ID and the handle stayed at 16/16 (`bench/results/p1-payload-length*`,
  `bench/results/P1-NOTES.md`; synthetic images, n=16 per cell). Nothing else about the tool's
  robustness claims changed with `--id`.
- **The hidden ID is read with a decoder that knows what an ID looks like.** An ID is always 112 bits
  on the wire, so `extract` doesn't hunt for the period (the text decoder needs one repeat's 32-bit
  header to survive bit-exact — with a noisy channel that fails long before the *sum* of the repeats
  does): it sums the repeats at each of the 112 possible starting phases and accepts only a canonical
  ID whose check characters verify (`wmcore.find_spread_spectrum_id`). Measured against the text
  decoder on the same attacked images (`bench/results/P2-NOTES.md`; synthetic images and 7 classic
  test photos — a direction, not a rate): **inside the documented range the gain is small** (768/768 vs
  765/768 on synthetic images, 112/112 both on the photos); it shows at the margin — JPEG q30, blur 1.5,
  and a JPEG q20 re-save through the full pipeline (0/6 → 4/6): 17 more images read, none fewer, in 1968
  paired synthetic trials. It never returned a wrong string (the text decoder returned 28, 24 of them on
  crops it isn't built for), and 0/400 synthetic and 0/28 photo mark-free images produced an ID. **The
  cost:** a wrong key reads the *right* ID more often — 29% of wrong keys on synthetic images (vs 17% for
  the text decoder; 24% vs 21% on the 7 photos, a difference that size can't resolve). It is the true ID,
  never a different one, but it is one more reason not to lean on `--ss-key` as a secret. `--rescale` reads
  with it too, at every candidate size (`bench/results/P2-NOTES.md` §6): on resized copies it read 8 more
  synthetic and 3 more photo trials than the text decoder and lost none — but those come from 3 of 24
  synthetic images and 2 of 7 photos, all of them cases where the text decoder had lost a mark that was
  there. The photos' ×0.5 misses are unchanged, and crop + resize was not measured. On never-stamped periodic
  patterns (checkerboards, stripes, grid lines; 10 hand-made images) the text decoder returned junk — accepted as
  a payload in 2 of 30 searches, both from the plain decode of a grid-lines image — while the ID reader never
  returned an ID (0 in 660 decode attempts; its own search accepted 0/30): a sign that the text decoder's false
  positives are real, not a rate. Wrong keys still read the true ID through the resize search about one time in
  five (23% vs 19% for the text decoder at 320×240, n=100, intervals overlapping).
- **Keep the ledger.** It is what turns an ID back into a file, a date and a key. Back it up; don't
  publish it (it holds keys). Lose it and the IDs are still readable, but nothing says what they mean.
  Local disk only — SQLite file locking is unreliable on network filesystems.
- **`--grid-id` makes the grid text longer** (wider tiles, a little more conspicuous). Measured effect on
  the hidden spread mark: none detectable — 16/16 in every configuration at 640×480 after identity, JPEG
  q60, JPEG q40 and a 0.75× resize with `--rescale`; at 1280×960 `gradnoise` the resize-recovery rate was
  3/10 for the legacy payload, for `--id` and for `--id --grid-id` alike (n=10, intervals wide). That 30%
  is the resize search's existing limit at this size — **and it comes from the visible grid itself, not
  from `--id`, the image content, or a general "large images are worse" rule.** The grid's tile
  `spacing`/`font_size` are fixed pixel values (not scaled to image dimensions), so which part of the
  tiled pattern lands at the image's top-left corner — the one spot the resize search's cheap scale-sweep
  statistic looks at — depends on image size. At 1280×960 that lands badly for `gradnoise`: turning the
  grid off (nothing else changed) takes that cell from 0/12 to 12/12; at 640×480 the grid never hurts
  (12/12 either way); a plain, unresized decode is unaffected by the grid at any size (12/12) — only the
  resize-search's corner-anchored statistic is fooled. `pink`'s own texture partly masks it (8-10/12
  either way, not the same total wipeout). Confirmed on one real photo too: a photographed checkerboard
  (`board.jpg`, strongly periodic content, same mechanism as the tiled grid) is the one real image in a
  small real-photo run that failed `resize_0.75 (+rescale)`. Not fixed — see
  `bench/results/P0-NOTES.md` §1 for the full account, the reproduction command
  (`bench/experiments/grid_corner_anchor.py`), and untried fix ideas (multi-point anchoring; scaling the
  grid to image size). Details in `bench/results/P1-NOTES.md`.
- **The web page's client-side mode has no ledger** (it is a static canvas approximation). In *Full
  pipeline* mode the server records into its own ledger (`serve.py --ledger`); a request can't choose the
  ledger file, and `/api/extract` returns the record without the key or settings.
