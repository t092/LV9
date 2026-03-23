from PIL import Image
img = Image.open('CH2MAP.jpg')
width, height = img.size
pixels = img.load()

white_pixels = []
for y in range(height):
    for x in range(width):
        p = pixels[x, y]
        if isinstance(p, tuple) and len(p) >= 3:
            if p[0] > 240 and p[1] > 240 and p[2] > 240:
                white_pixels.append((x, y))

print(f"Found {len(white_pixels)} white pixels (Image size: {width}x{height})")
