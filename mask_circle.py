from PIL import Image, ImageDraw

img = Image.open('images/mexican-mascot.png').convert("RGBA")
w, h = img.size

# Create a high-res mask for antialiasing
scale = 4
mask = Image.new('L', (w * scale, h * scale), 0)
draw = ImageDraw.Draw(mask)

# The image is circular. Let's draw a circle that touches the edges.
# We'll inset it slightly (e.g., 2 pixels) to ensure we don't catch any black border
inset = 2
draw.ellipse((inset * scale, inset * scale, (w - inset) * scale, (h - inset) * scale), fill=255)

# Downsample the mask
mask = mask.resize((w, h), Image.LANCZOS)

# Apply the mask to the alpha channel
result = img.copy()
# We want to keep the original alpha of the image if it had one, but it has a black background
# So we just use our circle mask
result.putalpha(mask)

result.save('images/mexican-mascot.png')
print("Successfully applied circular mask!")
