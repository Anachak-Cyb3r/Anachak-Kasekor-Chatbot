from PIL import Image
import os

# Open the image
img = Image.open('img/intro.png')

# Get original size
original_size = os.path.getsize('img/intro.png') / (1024 * 1024)
print(f"Original size: {original_size:.2f} MB")

# Resize if too large (keep aspect ratio)
max_width = 1280
if img.width > max_width:
    ratio = max_width / img.width
    new_height = int(img.height * ratio)
    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    print(f"Resized to: {max_width}x{new_height}")

# Convert to RGB if necessary
if img.mode in ('RGBA', 'LA', 'P'):
    background = Image.new('RGB', img.size, (255, 255, 255))
    if img.mode == 'P':
        img = img.convert('RGBA')
    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
    img = background

# Save with compression
img.save('img/intro_compressed.jpg', 'JPEG', quality=85, optimize=True)

# Check new size
new_size = os.path.getsize('img/intro_compressed.jpg') / (1024 * 1024)
print(f"Compressed size: {new_size:.2f} MB")
print(f"Reduction: {((original_size - new_size) / original_size * 100):.1f}%")
