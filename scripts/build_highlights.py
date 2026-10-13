# /// script
# dependencies = ["pillow"]
# ///
"""Compose the HIGHLIGHTS.md tiles into the single README GIF.

Usage: uv run scripts/build_highlights.py
Tiles are 400x225 GIFs in assets/highlights/, listed in the same order as HIGHLIGHTS.md.
Shorter tiles loop until the longest one ends.
"""
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
TILES = [
    ("digimon-survivor", "Digimon Survivor"),
    ("ai-novel-studio", "AI Novel Studio"),
    ("mango-orchard-defense", "Mango Orchard Defense"),
    ("ai-shorts", "AI Shorts"),
    ("at-badminton-cup", "AT Badminton Cup"),
    ("stock-news-radar", "stock-news-radar"),
]
W, H, LABEL, GAP, COLS = 400, 225, 30, 8, 2
FPS, COLORS, SECONDS = 8, 64, 8
BG = "0x0d1117"
FONTS = ["/System/Library/Fonts/HelveticaNeue.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]


def font():
    for path in FONTS:
        if Path(path).exists():
            return ImageFont.truetype(path, 16)
    return ImageFont.load_default()


def label(text, out):
    img = Image.new("RGB", (W, LABEL), "#0d1117")
    ImageDraw.Draw(img).text((10, LABEL // 2), text, fill="#e6edf3", font=font(), anchor="lm")
    img.save(out)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        args, chains, cells = [], [], []
        for i, (name, title) in enumerate(TILES):
            png = Path(tmp) / f"{i}.png"
            label(title, png)
            args += ["-ignore_loop", "0", "-i", str(ROOT / "assets/highlights" / f"{name}.gif"), "-loop", "1", "-i", str(png)]
            chains.append(f"[{2*i}]fps={FPS},trim=0:{SECONDS},setpts=PTS-STARTPTS[t{i}];"
                          f"[{2*i+1}]fps={FPS},trim=0:{SECONDS}[l{i}];[t{i}][l{i}]vstack[c{i}]")
            x, y = (i % COLS) * (W + GAP) + GAP, (i // COLS) * (H + LABEL + GAP) + GAP
            cells.append(f"{x}_{y}")
        rows = -(-len(TILES) // COLS)
        size = f"{COLS * (W + GAP) + GAP}x{rows * (H + LABEL + GAP) + GAP}"
        inputs = "".join(f"[c{i}]" for i in range(len(TILES)))
        graph = ";".join(chains) + (
            f";color=c={BG}:s={size}:r={FPS}:d={SECONDS}[bg];"
            f"{inputs}xstack=inputs={len(TILES)}:layout={'|'.join(cells)}:fill={BG}[grid];"
            f"[bg][grid]overlay=0:0:shortest=1,split[a][b];"
            f"[a]palettegen=max_colors={COLORS}:stats_mode=diff[p];"
            f"[b][p]paletteuse=dither=none:diff_mode=rectangle"
        )
        out = ROOT / "assets/highlights.gif"
        subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", graph, "-t", str(SECONDS), str(out)], check=True)
        print(f"{out.relative_to(ROOT)}: {out.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
