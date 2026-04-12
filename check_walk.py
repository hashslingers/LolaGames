#!/usr/bin/env python3
"""
Generate a walk animation strip and game-scale preview after the col 2/3 swap.
Shows: walk col1, walk col2 (was col3 — clean stride), walk col3 (was col2 — wide, now unused)
"""
from PIL import Image, ImageDraw, ImageFont

PATH = '/Users/js/Documents/LolaGame/Lola-bit.png'
OUT_DIR = '/Users/js/Documents/LolaGame/sprite_cells/'

CELL_W, CELL_H = 480, 548
LOLA_SCALE_OLD = 0.22
LOLA_SCALE_NEW = 0.28

img = Image.open(PATH).convert('RGBA')

# ── Walk frames at new game scale ──────────────────────────────────────────
new_w = int(CELL_W * LOLA_SCALE_NEW)
new_h = int(CELL_H * LOLA_SCALE_NEW)

print(f"New render size: {new_w}x{new_h}")

frames = []
for col in [1, 2, 3]:  # col1=pose, col2=clean stride (after swap), col3=wide (unused)
    x = col * CELL_W
    cell = img.crop((x, 0, x + CELL_W, CELL_H))
    thumb = cell.resize((new_w, new_h), Image.LANCZOS)
    frames.append(thumb)

# Build comparison strip with labels
pad = 8
label_h = 20
strip_w = (new_w + pad) * 3 + pad
strip_h = new_h + label_h + pad * 2
bg_color = (80, 80, 80, 255)

strip = Image.new('RGBA', (strip_w, strip_h), bg_color)
labels = ['col1 (pose)', 'col2 ✓ stride', 'col3 (unused)']

for i, (frame, label) in enumerate(zip(frames, labels)):
    x = pad + i * (new_w + pad)
    y = label_h + pad
    # Checkerboard bg behind frame
    cb = Image.new('RGBA', (new_w, new_h), (200, 200, 200, 255))
    for ty in range(0, new_h, 12):
        for tx in range(0, new_w, 12):
            if (tx//12 + ty//12) % 2 == 0:
                for py in range(ty, min(ty+12, new_h)):
                    for px in range(tx, min(tx+12, new_w)):
                        cb.putpixel((px, py), (160, 160, 160, 255))
    cb.paste(frame, (0, 0), frame)
    strip.paste(cb, (x, y))

    # Label text via draw
    draw = ImageDraw.Draw(strip)
    draw.text((x + new_w//2, pad//2), label, fill=(255, 255, 255, 255), anchor='mt')

strip.save(OUT_DIR + 'walk_new_scale.png')
print(f"Saved: {OUT_DIR}walk_new_scale.png")

# ── Also make a quick animated GIF at new scale ──────────────────────────
anim_frames = frames[:2]  # only col1 and col2 (the 2-frame walk cycle)
anim_bg = Image.new('RGBA', (new_w, new_h), (120, 180, 120, 255))
pil_frames = []
for f in anim_frames:
    bg = anim_bg.copy()
    bg.paste(f, (0, 0), f)
    pil_frames.append(bg.convert('RGB'))

pil_frames[0].save(
    OUT_DIR + 'walk_new_anim.gif',
    save_all=True, append_images=pil_frames[1:],
    duration=int(1000/8), loop=0
)
print(f"Saved: {OUT_DIR}walk_new_anim.gif")

# ── Character width analysis ──────────────────────────────────────────────
print("\nCharacter width analysis at new scale:")
for col_idx, col in enumerate([1, 2, 3]):
    x = col * CELL_W
    cell = img.crop((x, 0, x + CELL_W, CELL_H))
    pixels = cell.load()
    min_x = CELL_W
    max_x = 0
    for cy in range(CELL_H):
        for cx in range(CELL_W):
            r, g, b, a = pixels[cx, cy]
            spread = max(r, g, b) - min(r, g, b)
            avg = (r + g + b) / 3.0
            if a > 30 and not (avg > 40 and spread < 18):
                if cx < min_x: min_x = cx
                if cx > max_x: max_x = cx
    span = max_x - min_x + 1 if max_x > min_x else 0
    rendered = int(span * LOLA_SCALE_NEW)
    label = labels[col_idx]
    status = "✓ clean" if rendered <= new_w * 0.75 else "⚠ WIDE"
    print(f"  {label}: spans {min_x}-{max_x} = {span}px source → {rendered}px rendered {status}")

print(f"\nCell render size: {new_w}x{new_h}px (LOLA_SCALE=0.28)")
