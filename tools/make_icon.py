#!/usr/bin/env python3
"""Draw the directory listing icon: plugin/.claude-plugin/icon.png.

    python3 tools/make_icon.py

A round icon: a disc of the ACCEL2 hydrodynamical density field inside a navy
border and a thin white ring, transparent outside. No text, since it would be
unreadable at 64 px. Deterministic: the same file each run.

`tools/icon-background.png` is the central 480 px square of the ACCEL2 visual
(Chabanier, Ravoux et al. 2024) that the opendeck slides use as background
(`opendeck-decks/*/media/7c47c394bed8be7096e2.png`, 2140 x 1204).

Needs Pillow; this script is a maintainer tool and stays outside plugin/.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "plugin" / ".claude-plugin" / "icon.png"
BACKGROUND = Path(__file__).resolve().parent / "icon-background.png"
SIZE = 1024
SCALE = 4  # draw large, then downsample for smooth edges

NAVY = (11, 29, 58)
WHITE = (240, 244, 250)


def disc(image: Image.Image, radius: float) -> Image.Image:
    """Return the image cut to a centred disc, transparent outside."""
    size = image.size[0]
    centre = size / 2
    mask = Image.new("L", image.size, 0)
    ImageDraw.Draw(mask).ellipse([centre - radius, centre - radius, centre + radius, centre + radius], fill=255)
    out = Image.new("RGBA", image.size, (0, 0, 0, 0))
    out.paste(image, (0, 0), mask)
    return out


def draw() -> Image.Image:
    big = SIZE * SCALE
    centre = big / 2
    border, field_radius, ring_radius, ring = big * 0.49, big * 0.42, big * 0.475, big * 0.014

    image = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    ImageDraw.Draw(image).ellipse([centre - border, centre - border, centre + border, centre + border], fill=NAVY + (255,))
    field = Image.open(BACKGROUND).convert("RGB").resize((big, big), Image.Resampling.BICUBIC)
    field = Image.blend(field, Image.new("RGB", (big, big), NAVY), 0.15)
    image = Image.alpha_composite(image, disc(field, field_radius))
    ImageDraw.Draw(image).ellipse([centre - ring_radius, centre - ring_radius, centre + ring_radius, centre + ring_radius],
                                  outline=WHITE, width=int(ring))
    return image.resize((SIZE, SIZE), Image.Resampling.LANCZOS)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    draw().save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
