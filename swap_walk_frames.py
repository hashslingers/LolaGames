#!/usr/bin/env python3
"""
Swap row 0 col 2 and col 3 in Lola-bit.png.

Walk animation currently uses row=0, col=1..3 (3 frames).
Col 2 spans the FULL cell width (478px), looking like two separate figures at game scale.
Col 3 is a clean stride frame.

After swap: col 1 = good pose, col 2 = clean stride (was col 3), col 3 = wide frame (unused).
Then change walk to frames: 2 so it uses only col 1 and col 2.
"""
from PIL import Image

PATH = '/Users/js/Documents/LolaGame/Lola-bit.png'

CELL_W, CELL_H = 480, 548

img = Image.open(PATH).convert('RGBA')
w, h = img.size
print(f"Sprite: {w}x{h}")

# Extract col 2 and col 3 from row 0
row = 0
col2_x = 2 * CELL_W
col3_x = 3 * CELL_W
cell_y = row * CELL_H

cell2 = img.crop((col2_x, cell_y, col2_x + CELL_W, cell_y + CELL_H)).copy()
cell3 = img.crop((col3_x, cell_y, col3_x + CELL_W, cell_y + CELL_H)).copy()

print(f"Row 0, Col 2 size: {cell2.size}")
print(f"Row 0, Col 3 size: {cell3.size}")

# Swap them: put col3 at col2 position, col2 at col3 position
img.paste(cell3, (col2_x, cell_y))
img.paste(cell2, (col3_x, cell_y))

img.save(PATH)
print(f"Swapped col 2 and col 3 in row 0.")
print(f"Saved: {PATH}")
print()
print("Now update lola_game.html:")
print("  walk: { row: 0, col: 1, frames: 2, fps: 8 },  // col1=pose, col2=stride (was col3)")
print("  const LOLA_SCALE = 0.28;  // bigger character")
