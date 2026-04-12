#!/usr/bin/env python3
"""
Remove checkerboard background from Lola-bit.png.
The checkerboard is baked as near-neutral gray pixels (R≈G≈B, mid-range).
Character pixels have real hue (warm skin, brown hair, blue sweater, pink).
"""
from PIL import Image
import os

INPUT  = '/Users/js/Documents/LolaGame/Lola-bit.png'
OUTPUT = '/Users/js/Documents/LolaGame/Lola-bit.png'
BACKUP = '/Users/js/Documents/LolaGame/Lola-bit-original.png'

img = Image.open(INPUT).convert('RGBA')
w, h = img.size
print(f"Image size: {w}x{h}, mode: {img.mode}")

# Sample corners to identify background color
corners = [img.getpixel((0,0)), img.getpixel((w-1,0)),
           img.getpixel((0,h-1)), img.getpixel((w-1,h-1))]
print(f"Corner pixels: {corners}")

# Back up original if not already done
if not os.path.exists(BACKUP):
    img.save(BACKUP)
    print(f"Backup saved: {BACKUP}")

pixels = img.load()
removed = 0
total = w * h

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if a < 5:
            continue  # already transparent

        hi = max(r, g, b)
        lo = min(r, g, b)
        spread = hi - lo          # 0 = pure gray, higher = real color
        avg = (r + g + b) / 3.0

        # Checkerboard: near-neutral gray, mid-to-light range
        # Real character pixels have warm hue (spread > 30 typically)
        if avg > 110 and avg < 255 and spread < 50:
            # Gradient removal: pure gray → fully transparent, edge → partial
            grayness = max(0.0, 1.0 - spread / 50.0) ** 1.5
            new_alpha = int(a * (1.0 - grayness))
            if new_alpha < a:
                pixels[x, y] = (r, g, b, new_alpha)
                removed += 1

print(f"Pixels modified: {removed} / {total} ({removed/total*100:.1f}%)")

img.save(OUTPUT)
print(f"Saved: {OUTPUT}")
print("Done! Checkerboard removed.")
