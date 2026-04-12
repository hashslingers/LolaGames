#!/usr/bin/env python3
"""
Inspect all rows to find the cleanest animation frames.
Shows opaque pixel count, span, and generates thumbnails for each row.
"""
from PIL import Image, ImageDraw

PATH = '/Users/js/Documents/LolaGame/Lola-bit.png'
CELL_W, CELL_H = 480, 548
ROWS, COLS = 4, 4
SCALE = 0.35  # thumbnail scale

img = Image.open(PATH).convert('RGBA')

tw = int(CELL_W * SCALE)
th = int(CELL_H * SCALE)

for row in range(ROWS):
    print(f"\n── Row {row} ──────────────────────────────")
    # Create a strip for this row
    strip = Image.new('RGBA', (tw * COLS + (COLS-1) * 4, th + 20), (50, 50, 50, 255))
    draw = ImageDraw.Draw(strip)

    for col in range(COLS):
        x = col * CELL_W
        y = row * CELL_H
        cell = img.crop((x, y, x + CELL_W, y + CELL_H))
        pixels = cell.load()

        # Find connected regions: simple column-based analysis
        # For each x-column, find opaque pixels
        col_counts = []
        for cx in range(CELL_W):
            count = sum(1 for cy in range(CELL_H) if pixels[cx, cy][3] > 30)
            col_counts.append(count)

        # Find bounding box
        min_x = min_y = CELL_W
        max_x = max_y = 0
        total_opaque = 0
        for cy in range(CELL_H):
            for cx in range(CELL_W):
                if pixels[cx, cy][3] > 30:
                    total_opaque += 1
                    if cx < min_x: min_x = cx
                    if cx > max_x: max_x = cx
                    if cy < min_y: min_y = cy
                    if cy > max_y: max_y = cy

        # Find gap in the middle (empty x-columns between characters)
        center = CELL_W // 2
        # Find biggest gap: look for runs of low pixel-count columns
        gaps = []
        in_gap = False
        gap_start = 0
        for cx in range(CELL_W):
            if col_counts[cx] < 5:
                if not in_gap:
                    gap_start = cx
                    in_gap = True
            else:
                if in_gap:
                    gaps.append((gap_start, cx - 1, cx - gap_start))
                    in_gap = False
        if in_gap:
            gaps.append((gap_start, CELL_W - 1, CELL_W - gap_start))

        # Find largest gap that's not at the edges
        inner_gaps = [(s, e, l) for s, e, l in gaps if s > 20 and e < CELL_W - 20]
        max_gap = max(inner_gaps, key=lambda g: g[2]) if inner_gaps else None

        if max_x > min_x:
            span = max_x - min_x + 1
            cx_center = (min_x + max_x) // 2
        else:
            span = cx_center = 0

        gap_info = f"  gap@{max_gap[0]}-{max_gap[1]}(w={max_gap[2]})" if max_gap else ""
        clean = "✓ CLEAN" if (not max_gap or max_gap[2] < 20) else f"⚠ SPLIT at x={max_gap[0]}"
        print(f"  col{col}: opaque={total_opaque}, span={span}px, center_x={cx_center}{gap_info} {clean}")

        # Thumbnail
        bg = Image.new('RGBA', (tw, th), (180, 180, 180, 255))
        for ty2 in range(0, th, 12):
            for tx2 in range(0, tw, 12):
                if (tx2//12 + ty2//12) % 2 == 0:
                    for py in range(ty2, min(ty2+12, th)):
                        for px in range(tx2, min(tx2+12, tw)):
                            bg.putpixel((px, py), (140, 140, 140, 255))
        thumb = cell.resize((tw, th), Image.LANCZOS)
        bg.paste(thumb, (0, 0), thumb)
        strip.paste(bg, (col * (tw + 4), 0))
        draw.text((col * (tw + 4) + tw//2, th + 2), f'r{row}c{col}', fill=(200,200,200), anchor='mt')

    strip.save(f'/Users/js/Documents/LolaGame/sprite_cells/row{row}_strip.png')
    print(f"  → saved row{row}_strip.png")
