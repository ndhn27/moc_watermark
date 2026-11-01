"""Small, dependency-free building blocks shared across the other wmcore
submodules: font loading, path/extension constants, seed derivation, and
payload bit-packing.
"""

import os
import zlib

from PIL import Image, ImageFont

DEFAULT_FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux/WSL2
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",      # macOS (Catalina+, stock)
    "/Library/Fonts/Arial Bold.ttf",                          # macOS (older / MS Office install)
    "C:\\Windows\\Fonts\\arialbd.ttf",                         # Windows fallback
]

VIDEO_EXTS = (".mp4", ".mov", ".m4v", ".avi", ".mkv", ".webm")
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff")

# Output formats that cannot carry transparency, so an RGBA image has to be laid on a background before it is
# saved. JPEG has no alpha at all. BMP is the odd one: Pillow writes a 32-bit file whose fourth byte is the alpha,
# but its own reader (and most viewers) ignore that byte and show the colour underneath - for a transparent PNG
# that is usually black. PNG, WebP and TIFF keep alpha and are not in this list.
OPAQUE_ONLY_EXTS = (".jpg", ".jpeg", ".bmp")

# White, the same fill the web page paints behind the picture before it exports a JPEG (web/index.html, redrawFor).
FLATTEN_BACKGROUND = (255, 255, 255)

_font_fallback_warned = False


def load_font(font_size, font_path=None):
    """Load a TrueType font, trying `font_path` (if given) then the
    platform-default candidates in DEFAULT_FONT_PATHS, in order.

    Falls back to PIL's built-in default font at `font_size` (Pillow >= 10.1
    only - older Pillow's `load_default()` ignores the size and is
    tiny/blocky; that case prints a one-time warning instead of one per file).
    """
    global _font_fallback_warned
    candidates = [font_path] if font_path else DEFAULT_FONT_PATHS
    for path in candidates:
        if path and os.path.exists(path):
            return ImageFont.truetype(path, font_size)
    try:
        return ImageFont.load_default(size=font_size)
    except TypeError:
        pass  # Pillow < 10.1: load_default() doesn't take a size argument
    if not _font_fallback_warned:
        checked = ", ".join(p for p in candidates if p)
        print(
            f"Warning: no TrueType font found (checked: {checked}) and this Pillow "
            "version's built-in fallback font is fixed-size. Text will be tiny and "
            "won't scale with --font-size. Pass --font-path /path/to/font.ttf, or "
            "upgrade Pillow to >=10.1, to fix this."
        )
        _font_fallback_warned = True
    return ImageFont.load_default()


def derive_seed(base_seed, key):
    """Deterministically derive a distinct-but-reproducible seed from a base
    seed and a key (a filename, a video segment index, etc.), so several
    items sharing one base seed each get their own jitter pattern instead of
    an identical, averageable one. Returns None unchanged when base_seed is
    None.

    Uses crc32 rather than the built-in hash(): Python salts string hashing
    per-process by default, which would break run-to-run reproducibility.
    """
    if base_seed is None:
        return None
    return base_seed + (zlib.crc32(str(key).encode("utf-8")) % 100000)


def text_to_bits(text):
    """UTF-8 encode `text` and prefix a 4-byte big-endian length header,
    returned as a flat list of bits (MSB first). Shared wire format for both
    the LSB and spread-spectrum invisible marks.
    """
    payload = text.encode("utf-8")
    header = len(payload).to_bytes(4, "big")
    data = header + payload
    bits = []
    for byte in data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return bits


def rgba_keeping_alpha(rgb_image, source):
    """`rgb_image` (a PIL image the embedders built from RGB arrays) as RGBA, carrying over `source`'s alpha.

    Image.convert("RGBA") from RGB makes every pixel opaque, so an embedder that works on RGB and
    converts back would turn a transparent PNG into an opaque one. The hidden marks only touch the
    colour channels; the transparency belongs to the caller's image and goes back unchanged.
    `source` may be RGBA/LA/PA or a palette image with a transparency entry; anything else is opaque.
    """
    out = rgb_image.convert("RGBA")
    if "A" in source.getbands() or "transparency" in source.info:
        out.putalpha(source.convert("RGBA").getchannel("A"))
    return out


def drops_alpha(path):
    """Whether a file saved at `path` (judged by its extension, like the rest of this tool) cannot keep transparency."""
    return path.lower().endswith(OPAQUE_ONLY_EXTS)


def has_transparency(image):
    """Whether any pixel of `image` is not fully opaque. Handles RGBA/LA/PA, premultiplied bands, and palette, L
    or RGB images that carry a transparency entry; an image with none of those is opaque without looking at pixels.
    """
    bands = image.getbands()
    if "A" in bands or "a" in bands or "transparency" in image.info:
        return image.convert("RGBA").getchannel("A").getextrema()[0] < 255
    return False


def flatten_alpha(image, background=FLATTEN_BACKGROUND):
    """`image` as an opaque RGB image: transparent parts become `background`, partly transparent ones are blended
    with it (straight alpha, in the stored sRGB values, which is what every viewer and the web page do).

    This is what JPEG/BMP output needs. Dropping the alpha band instead (Image.convert("RGB")) shows whatever
    colour sits under a transparent pixel - black for most exporters - and shows half-transparent pixels as if
    they were solid. A fully opaque image comes back unchanged, pixel for pixel. `background` is an (r, g, b) tuple.
    """
    if not has_transparency(image):
        return image.convert("RGB")
    rgba = image.convert("RGBA")
    canvas = Image.new("RGBA", rgba.size, tuple(background) + (255,))
    return Image.alpha_composite(canvas, rgba).convert("RGB")
