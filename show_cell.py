#!/usr/bin/env python3
"""Show each row0 cell at FULL half-size (240x274) individually to diagnose."""
from PIL import Image

PATH = '/Users/js/Documents/LolaGame/Lola-bit.png'
CELL_W, CELL_H = 480, 548

img = Image.open(PATH).convert('RGBA')

for col in range(4):
    x = col * CELL_W
    cell = img.crop((x, 0, x + CELL_W, CELL_H))

    # Count non-transparent pixels
    pixels = cell.load()
    opaque = 0
    for cy in range(CELL_H):
        for cx in range(CELL_W):
            if pixels[cx, cy][3] > 30:
                opaque += 1

    # Find bounding box of visible content
    min_x, min_y, max_x, max_y = CELL_W, CELL_H, 0, 0
    for cy in range(CELL_H):
        for cx in range(CELL_W):
            if pixels[cx, cy][3] > 30:
                if cx < min_x: min_x = cx
                if cx > max_x: max_x = cx
                if cy < min_y: min_y = cy
                if cy > max_y: max_y = cy

    if max_x > min_x:
        span_w = max_x - min_x + 1
        span_h = max_y - min_y + 1
        center_x = (min_x + max_x) // 2
    else:
        span_w = span_h = center_x = 0

    print(f"Row0 Col{col}: opaque_px={opaque}, bounds=({min_x},{min_y})-({max_x},{max_y}), span={span_w}x{span_h}, center_x={center_x}")

    # Save at full 50% scale
    out = f'/Users/js/Documents/LolaGame/sprite_cells/row0_col{col}_large.png'
    bg = Image.new('RGBA', (CELL_W//2, CELL_H//2), (180, 180, 180, 255))
    # checkerboard bg
    for ty in range(0, CELL_H//2, 20):
        for tx in range(0, CELL_W//2, 20):
            if (tx//20 + ty//20) % 2 == 0:
                for py in range(ty, min(ty+20, CELL_H//2)):
                    for px in range(tx, min(tx+20, CELL_W//2)):
                        bg.putpixel((px, py), (140, 140, 140, 255))
    thumb = cell.resize((CELL_W//2, CELL_H//2), Image.LANCZOS)
    bg.paste(thumb, (0, 0), thumb)
    bg.save(out)
    print(f"  → saved {out}")
