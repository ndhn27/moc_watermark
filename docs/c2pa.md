# C2PA (Content Credentials)

[← Back to the README](../README.md)

`--c2pa` signs the output with a [C2PA](https://c2pa.org/) manifest — a
cryptographically signed record binding a claim ("this file, watermarked,
edited from that parent file, by this action") to the file's actual bytes.
It's genuinely different from every other mechanism in this tool (see the
callout in the [feature list](../README.md#features) and the [Threat model](threat-model.md#threat-model) section): the grid, jitter, and
invisible marks all ask "did a recoverable trace of the pattern survive
whatever happened to this image", a pixel-robustness question with no
hard guarantee. C2PA instead asks "does this exact file's content match a
manifest that was cryptographically signed at edit time" — editing the
pixels at all invalidates the signature rather than maybe surviving it, and
because it applies to the file as a signed data structure rather than to
pixel patterns, it works identically for **video**, not just images (unlike
`--author`/`--copyright`'s own file-format-metadata role, and unlike
`--invisible-mode lsb`, all image-only — `--invisible-mode spread` does
work for video, see [Video support](video.md#video-support)).

```bash
# sign with the auto-generated local dev certificate (zero setup)
python3 cli/watermark.py in.jpg out.jpg --text "@yourhandle" --c2pa

# same, plus an author recorded in the manifest's CreativeWork assertion
# (works for video too, even though --author's OWN EXIF/PNG-metadata role
# elsewhere in this tool stays image-only)
python3 cli/watermark.py in.mp4 out.mp4 --text "@yourhandle" --c2pa --author "Your Name"

# read the manifest back
python3 cli/c2pa_verify.py out.jpg
python3 cli/c2pa_verify.py out.jpg --json   # full parsed detail
```

**Read this before showing a `--c2pa` file to anyone else.** By default,
signing uses a **local, self-signed certificate**, auto-generated on first
use and reused after that at `~/.watermark-tool/dev_cert.pem` (main() does
this once up front, not per file, so a `--batch` run's worker processes
all reuse the same identity rather than racing to generate their own). The
resulting signature is completely real — the hash-binding and signature
checks genuinely pass, and `c2pa_verify.py`'s `Validation state: Valid` on
it isn't a lie — but because nothing vouches for *the certificate itself*,
every C2PA-aware reader (`c2pa_verify.py` included) reports the signing
credential as **untrusted** rather than showing a verified checkmark:

```
Validation state: Valid
  - FAILED signingCredential.untrusted: signing certificate untrusted (expected for the auto-generated dev cert - see cli/c2pa_provenance.py / README.md)
```

That failure code is the *entire* gap between "real signature, unknown
signer" and a verified badge — there is no additional "is it actually
tampered with" check hiding behind it. To close that gap, get a
certificate from a CA in the [C2PA-approved trust
list](https://opensource.contentauthenticity.org/docs/c2pa-conformance/trust-lists)
and pass it in:

```bash
python3 cli/watermark.py in.jpg out.jpg --text "@yourhandle" \
    --c2pa --c2pa-cert your_chain.pem --c2pa-key your_key.pem --c2pa-alg es256
```

`--c2pa-cert`/`--c2pa-key` must be given together. `--c2pa-alg` (default
`es256`) only matters with your own cert — the auto-generated dev
certificate is ES256-only, and a different `--c2pa-alg` without
`--c2pa-cert`/`--c2pa-key` is ignored (with a note) rather than silently
mismatched against it. `--c2pa-title` sets the manifest's recorded title
(default: the output filename).

**What's actually in the manifest:** if the input file the watermark was
applied to still exists on disk at signing time, the manifest is built as
an **EDIT** with a `parentOf` ingredient pointing at it — which makes the
C2PA side auto-generate a `c2pa.opened` action (a hash-link back to that
parent) ahead of the explicit `c2pa.watermarked` action this tool adds
(a real, registered C2PA action ID, not a made-up one) — so a reader sees
an actual two-step edit history, not just an unqualified claim. Without a
locatable parent, it falls back to a plain CREATE. `--author`, when given,
becomes a `stds.schema-org.CreativeWork` assertion inside the signed
manifest (separate from, and not a replacement for, `--author`'s own
EXIF/PNG-metadata writing for images).

**Format support and failure handling:** C2PA signing covers JPEG, PNG,
and MP4/MOV/AVI/M4V, but **not every format this tool otherwise supports**
— `.bmp`, `.mkv`, and `.webm` aren't in c2pa-python's supported list. If
you ask for `--c2pa` on one of those, signing fails with a printed note
(*"C2PA signing failed for ...; the watermark itself was still saved
without a C2PA manifest"*) rather than losing the watermark work already
done or crashing a `--batch` run over it — same graceful-degradation shape
as a missing `piexif` install elsewhere in this tool. No timestamp
authority is contacted by default (that would mean a network call on every
signing operation, with a third-party service as a new point of failure);
see `cli/c2pa_provenance.py`'s module docstring if you want to wire one up
yourself for long-term timestamp-backed validity.

Needs `c2pa-python` and `cryptography` installed (`pip install -r
requirements.txt` — both are listed there, commented, since they're
opt-in). `--c2pa` fails fast with a clear message up front if they're
missing, rather than silently skipping the manifest the way an optional
feature elsewhere in this tool might.

**Version matters: use `c2pa-python` 0.37.3 – 0.37.10** (`requirements.txt` pins it). Newer releases
(0.37.12, 0.38.0) reject the `c2pa.watermarked` action this tool writes — they require a soft-binding assertion for a watermark
action, which the tool does not write yet — so with them `--c2pa` reports that the file was not signed, and 0.37.0 / 0.37.1 raise a
`TypeError` in the signer. Measured: the C2PA tests pass on 0.37.3, 0.37.6, 0.37.9 and 0.37.10 and fail on 0.37.1, 0.37.12 and 0.38.0
(0.37.2, 0.37.4, 0.37.5, 0.37.7, 0.37.8 not tried). Writing the soft-binding assertion, so that a current release works, is open.
