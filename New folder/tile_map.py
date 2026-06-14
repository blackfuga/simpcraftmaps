from PIL import Image
import os, math

# ── CONFIGURE HERE ──────────────────────────────
INPUT_IMAGE = "bigmap.png"   # your exported Xaero PNG (put it in the same folder as this script)
OUTPUT_DIR  = "tiles"        # where tiles will be saved
MIN_ZOOM    = 0
MAX_ZOOM    = 9              # increase for more zoom levels (takes longer)
TILE_SIZE   = 256
# ────────────────────────────────────────────────

def make_tiles(img, zoom, out_dir):
    scale = 2 ** zoom
    w = TILE_SIZE * scale
    h = TILE_SIZE * scale
    resized = img.resize((w, h), Image.LANCZOS)

    total = scale * scale
    done  = 0
    for tx in range(scale):
        for ty in range(scale):
            left   = tx * TILE_SIZE
            top    = ty * TILE_SIZE
            right  = left + TILE_SIZE
            bottom = top  + TILE_SIZE
            tile   = resized.crop((left, top, right, bottom))

            tile_path = os.path.join(out_dir, str(zoom), str(tx))
            os.makedirs(tile_path, exist_ok=True)
            tile.save(os.path.join(tile_path, f"{ty}.png"))

            done += 1
            pct = done / total * 100
            print(f"  Zoom {zoom}: {pct:.0f}%  ({done}/{total} tiles)", end="\r")
    print()

def main():
    if not os.path.exists(INPUT_IMAGE):
        print(f"ERROR: Could not find '{INPUT_IMAGE}'")
        print(f"Make sure your PNG is in the same folder as this script and named '{INPUT_IMAGE}'")
        input("Press Enter to exit...")
        return

    print(f"Loading {INPUT_IMAGE}...")
    img = Image.open(INPUT_IMAGE).convert("RGBA")
    print(f"Image size: {img.width} x {img.height} px")

    # Make the image square (pad with black) so tiles line up correctly
    size = max(img.width, img.height)
    square = Image.new("RGBA", (size, size), (0, 0, 0, 255))
    square.paste(img, (0, 0))
    img = square

    print(f"\nGenerating tiles (zoom {MIN_ZOOM} to {MAX_ZOOM})...")
    for zoom in range(MIN_ZOOM, MAX_ZOOM + 1):
        num_tiles = (2 ** zoom) ** 2
        print(f"\nZoom level {zoom} ({num_tiles} tiles):")
        make_tiles(img, zoom, OUTPUT_DIR)

    print(f"\nDone! Tiles saved to '{OUTPUT_DIR}' folder.")
    print("Copy the 'tiles' folder into your 'mymap' folder, then upload to GitHub.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
