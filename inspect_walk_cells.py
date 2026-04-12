#!/usr/bin/env python3
"""
Generate large individual crops of the walk frames after the swap.
Shows all 4 cells in row 0 at 50% of original size for easy inspection.
"""
from PIL import Image

PATH = '/Users/js/Documents/LolaGame/Lola-bit.png'
OUT = '/Users/js/Documents/LolaGame/sprite_cells/row0_cells.png'

CELL_W, CELL_H = 480, 548
SCALE = 0.5  # 50% → 240x274 per cell

img = Image.open(PATH).convert('RGBA')

tw = int(CELL_W * SCALE)
th = int(CELL_H * SCALE)

# 4 cells across, show row 0
canvas = Image.new('RGBA', (tw * 4, th + 30), (60, 60, 60, 255))

for col in range(4):
    x = col * CELL_W
    cell = img.crop((x, 0, x + CELL_W, CELL_H))
    thumb = cell.resize((tw, th), Image.LANCZOS)

    # Checkerboard bg
    bg = Image.new('RGBA', (tw, th), (200, 200, 200, 255))
    for ty in range(0, th, 16):
        for tx in range(0, tw, 16):
            if (tx//16 + ty//16) % 2 == 0:
                for py in range(ty, min(ty+16, th)):
                    for px in range(tx, min(tx+16, tw)):
                        bg.putpixel((px, py), (160, 160, 160, 255))
    bg.paste(thumb, (0, 0), thumb)
    canvas.paste(bg, (col * tw, 0))

from PIL import ImageDraw
draw = ImageDraw.Draw(canvas)
labels = [
    'col0 (unused)',
    'col1 → IDLE + walk f1',
    'col2 → walk f2 (was col3)',
    'col3 (was col2, skip)',
]
for i, label in enumerate(labels):
    color = (100, 255, 100) if i in [1, 2] else (200, 200, 200)
    draw.text((i * tw + 4, th + 4), label, fill=color)

canvas.save(OUT)
print(f"Saved: {OUT}")
print(f"Cell render size at 50%: {tw}x{th}")
