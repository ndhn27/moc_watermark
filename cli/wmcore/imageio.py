"""One way to read an image file into memory, for the embedding side and for every reader.

Why not `Image.open(path)`: given a path, Pillow memory-maps an uncompressed single-strip TIFF (modes L, P, RGBA, CMYK,
...), and on that route an Orientation tag of 5-8 goes wrong - the pixel buffer is laid out with the DISPLAYED (swapped)
size instead of the stored one, so the size comes out swapped and the pixels scrambled, and `exif_transpose` cannot
repair it. Seen on Pillow 13.0.0 and 12.1.1; explained from Pillow's Python code (`ImageFile.load`, `TiffImagePlugin`)
and from experiments, NOT from the C code of `map_buffer`, which has not been read. A file object cannot be mapped, so
Pillow takes its ordinary decoder; Pillow's global `TiffImagePlugin.READ_LIBTIFF` flag is left alone. See docs/known-limitations.md
("Output formats", EXIF Orientation). Re-run bench/experiments/tiff_probe.py when Pillow is upgraded.

The embedding side and the readers must open images the same way: if the embedder sees the picture upright but a
reader sees it scrambled, a mark that was embedded correctly cannot be read back (measured: an uncompressed RGBA TIFF
stored sideways, Orientation 5-8, gave no LSB and no spread mark by path, and both through a file object). So there is
exactly one place that calls `Image.open` on a path, this one; tests/test_output_formats.py fails if another module does.
"""

from PIL import Image


def load_image(path, check=None):
    """The image at `path`, fully decoded into memory, with the file already closed.

    `check(image)`, if given, runs on the image as soon as its header is read and BEFORE any pixel is decoded (so a
    size limit can refuse a huge picture cheaply); whatever it raises propagates, and the file is closed either way.
    Apply no EXIF rotation here: the embedding side bakes it in itself (wmapp.pipeline), and the readers read the
    picture as it is stored, as they always did.
    """
    with open(path, "rb") as fp:
        img = Image.open(fp)
        if check is not None:
            check(img)
        img.load()
    return img
