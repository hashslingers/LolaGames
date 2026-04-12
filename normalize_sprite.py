#!/usr/bin/env python3
"""
Fix Lola-bit.png:
1. Remove checkerboard background (both light ~175 AND dark ~103 gray squares)
2. Normalize character position in each cell so:
   - Feet (character bottom) are at CELL_H * TARGET_FOOT_Y = consistent position
   - Character is horizontally centered in the cell
This eliminates the "doubles when running" jitter from inconsistent positions.
"""
from PIL import Image
import os

INPUT  = '/Users/js/Documents/LolaGame/Lola-bit-original.png'
OUTPUT = '/Users/js/Documents/LolaGame/Lola-bit.png'

CELL_W, CELL_H = 480, 548
ROWS, COLS = 4, 4
TARGET_FOOT_Y_RATIO = 0.93  # feet at 93% down the cell (matches LOLA_FOOT_OFFSET in JS)

def is_background(r, g, b, a):
    """Return True if pixel is checkerboard background (both light and dark gray squares)."""
    if a < 10:
        return True  # already transparent
    spread = max(r, g, b) - min(r, g, b)
    avg = (r + g + b) / 3.0
    # Checkerboard: near-neutral gray (both ~175 light and ~103 dark squares)
    # Real character pixels have distinct hue (spread >= 15) OR are very dark (avg < 40, outlines)
    if avg > 40 and spread < 18:
        return True
    return False

def remove_background(cell_img):
    """Remove checkerboard pixels, return RGBA image with clean transparency."""
    result = cell_img.copy().convert('RGBA')
    pixels = result.load()
    w, h = result.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            spread = max(r, g, b) - min(r, g, b)
            avg = (r + g + b) / 3.0
            if avg > 40 and spread < 18:
                # Gradient fade at edges (spread 12-18 = soft edge)
                grayness = max(0.0, 1.0 - spread / 18.0) ** 1.2
                new_a = int(a * (1.0 - grayness))
                pixels[x, y] = (r, g, b, new_a)
    return result

def find_char_bounds(cell_img):
    """Find bounding box of non-background pixels in a cell."""
    pixels = cell_img.load()
    w, h = cell_img.size
    min_x, min_y, max_x, max_y = w, h, 0, 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if not is_background(r, g, b, a):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    if min_x > max_x:  # no character found
        return None
    return min_x, min_y, max_x, max_y

def normalize_cell(cell_img):
    """
    Remove background and center the character so:
    - Feet (char bottom) are at TARGET_FOOT_Y_RATIO * CELL_H
    - Char is horizontally centered in the cell
    Returns a new CELL_W x CELL_H RGBA image.
    """
    cleaned = remove_background(cell_img)
    bounds = find_char_bounds(cell_img)

    if bounds is None:
        return Image.new('RGBA', (CELL_W, CELL_H), (0, 0, 0, 0))

    min_x, min_y, max_x, max_y = bounds
    char_w = max_x - min_x + 1
    char_h = max_y - min_y + 1
    char_cx = (min_x + max_x) // 2  # current center x

    # Target feet position
    target_foot_y = int(CELL_H * TARGET_FOOT_Y_RATIO)

    # Calculate where to paste the character
    # Current feet are at max_y. We want them at target_foot_y.
    dy = target_foot_y - max_y  # vertical shift

    # Current center is char_cx. We want it at CELL_W // 2.
    dx = (CELL_W // 2) - char_cx  # horizontal shift

    print(f"    bounds=({min_x},{min_y})-({max_x},{max_y}) center_x={char_cx} feet_y={max_y} → shift({dx},{dy})")

    # Create new blank cell and paste shifted character
    new_cell = Image.new('RGBA', (CELL_W, CELL_H), (0, 0, 0, 0))
    new_cell.paste(cleaned, (dx, dy), cleaned)
    return new_cell

# Load original
orig = Image.open(INPUT).convert('RGBA')
full_w, full_h = orig.size
print(f"Original sprite: {full_w}x{full_h}")
print(f"Cell size: {CELL_W}x{CELL_H}, Grid: {ROWS}x{COLS}")
print(f"Target foot Y: {int(CELL_H * TARGET_FOOT_Y_RATIO)} ({TARGET_FOOT_Y_RATIO*100:.0f}% of {CELL_H})")
print()

# Process each cell
output_img = Image.new('RGBA', (CELL_W * COLS, CELL_H * ROWS), (0, 0, 0, 0))

for row in range(ROWS):
    for col in range(COLS):
        ox, oy = col * CELL_W, row * CELL_H
        cell = orig.crop((ox, oy, ox + CELL_W, oy + CELL_H))

        print(f"Row {row}, Col {col}:")
        normalized = normalize_cell(cell)
        output_img.paste(normalized, (ox, oy))

output_img.save(OUTPUT)
print(f"\nSaved normalized sprite: {OUTPUT}")

# Also save a contact sheet of the result for visual check
thumb_w, thumb_h = 120, 137
contact = Image.new('RGBA', (thumb_w * COLS, thumb_h * ROWS), (80, 80, 80, 255))
for row in range(ROWS):
    for col in range(COLS):
        ox, oy = col * CELL_W, row * CELL_H
        cell = output_img.crop((ox, oy, ox + CELL_W, oy + CELL_H))
        thumb = cell.resize((thumb_w, thumb_h))
        # Add checkerboard bg for visibility
        bg = Image.new('RGBA', (thumb_w, thumb_h), (200, 200, 200, 255))
        for ty in range(0, thumb_h, 10):
            for tx in range(0, thumb_w, 10):
                if (tx//10 + ty//10) % 2 == 0:
                    for py in range(ty, min(ty+10, thumb_h)):
                        for px in range(tx, min(tx+10, thumb_w)):
                            bg.putpixel((px, py), (160, 160, 160, 255))
        bg.paste(thumb, (0, 0), thumb)
        contact.paste(bg, (col * thumb_w, row * thumb_h))

contact.save('/Users/js/Documents/LolaGame/sprite_cells/normalized_check.png')
print("Saved visual check: sprite_cells/normalized_check.png")
