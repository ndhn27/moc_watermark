# Threat model

[← Back to the README](../README.md)

Worth being explicit about what "removal-resistant" means here, because
it means different things depending on who's trying to remove the mark.

**What this defends against — casual / incidental removal.** Someone
crops the image, paints over part of it, takes a screenshot, re-uploads
through a platform that recompresses it, or just doesn't notice a
single corner logo. This is the everyday case the grid, the jitter, the
blend modes, content-adaptive placement, and the invisible backup marks
(`lsb` and `spread`) are built for, and it's a realistic bar to clear:
most removal in the wild is casual, not adversarial.

**What this does *not* defend against — a motivated adversary who knows
the scheme.** Per-tile jitter specifically defeats naive frequency-domain
estimation (FFT-averaging a fixed periodic pattern across many stamped
images), but that's one specific attack, not immunity in general. No
publicly known image watermarking technique — DCT/DWT, spread-spectrum
(this tool's own `spread` mode included), or learned marks like
HiDDEN/StegaStamp, including ones baked directly into a diffusion
model's seed (Tree-Ring, Gaussian Shading) — reliably survives someone
who deliberately targets it with tools like:

- **Regeneration / diffusion-purification attacks** — encode the image,
  add noise, and let a diffusion model (or VAE) resynthesize it; the
  reconstruction preserves perceptual content but not a low-amplitude
  watermark signal sitting off the "natural image" manifold. Zhao et al.
  gave a provable treatment of this and showed it empirically breaking
  several watermarking schemes (*"Invisible Image Watermarks Are
  Provably Removable Using Generative AI"*, NeurIPS 2024). Follow-up work
  extends the same idea to marks embedded in a diffusion model's own
  seed/latent rather than pixel space.
- **Collusion / averaging attacks** — with several images carrying a
  correlated pattern, simply averaging them out can estimate and
  subtract a "robust" watermark; this is the pixel-domain reason per-tile
  jitter matters here.
- **Adaptive / white-box optimization** — with access to the detector
  (or a good enough guess at the embedding scheme), directly optimizing
  a small perturbation to flip detection.
- **Desynchronization** — rotation, scaling, or local warping breaks
  correlation-based detectors unless they resynchronize first; a
  classical weakness predating any of the generative-AI attacks above.

`WAVES` (An et al., ICML 2024) standardizes exactly this kind of stress
test and found vulnerabilities in several widely-used watermarking
methods once regeneration and adversarial attacks were included
alongside ordinary distortions.

Provenance metadata (`--author`/`--copyright`) and manifest-style
schemes like C2PA (`--c2pa` — see the
[dedicated section](c2pa.md#c2pa-content-credentials)) sidestep the
pixel-robustness arms race entirely, but answer a different question —
"does this exact file match something signed" rather than "is a mark
still recoverable after edits" — so a full regeneration just produces
an unsigned image rather than a false match, which is a different
(arguably more honest) failure mode.

Bottom line: treat every mechanism in this tool as raising the cost of
casual removal, not as cryptographic proof against a determined,
resourced remover — that's still an open research problem industry-wide,
not a gap specific to this project.
