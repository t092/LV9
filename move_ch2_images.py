import os
import shutil

base_dir = r'c:\Users\grifo\OneDrive\AI\VibeVoding\CAI\LV9'
images_dir = os.path.join(base_dir, 'images')
ch2_dir = os.path.join(images_dir, 'ch2')

os.makedirs(ch2_dir, exist_ok=True)

# Files to move
files_to_move = [
    os.path.join(base_dir, 'CH2MAP.jpg'),
    os.path.join(images_dir, 'ch2-imperialism.jpg'),
    os.path.join(images_dir, 'ch2-alliances.jpg'),
    os.path.join(images_dir, 'ch2-sarajevo.jpg'),
    os.path.join(images_dir, 'ch2-trench.jpg'),
    os.path.join(images_dir, 'ch2-us-entry.jpg'),
    os.path.join(images_dir, 'ch2-versailles.jpg'),
    os.path.join(images_dir, 'ch2-league.jpg'),
    os.path.join(images_dir, 'asia_map_unmarked.jpg')
]

for f in files_to_move:
    if os.path.exists(f):
        basename = os.path.basename(f)
        dest = os.path.join(ch2_dir, basename)
        try:
            shutil.move(f, dest)
            print(f'Moved {basename} -> {dest}')
        except Exception as e:
            print(f'Failed to move {basename}: {e}')

# Update ch02.html
html_path = os.path.join(base_dir, 'ch02.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace "CH2MAP.jpg"
html = html.replace('"CH2MAP.jpg"', '"images/ch2/CH2MAP.jpg"')
# Replace "images/ch2-..."
for name in ['ch2-imperialism.jpg', 'ch2-alliances.jpg', 'ch2-sarajevo.jpg', 'ch2-trench.jpg', 'ch2-us-entry.jpg', 'ch2-versailles.jpg', 'ch2-league.jpg', 'asia_map_unmarked.jpg']:
    html = html.replace(f'"images/{name}"', f'"images/ch2/{name}"')
    html = html.replace(f"'{name}'", f"'images/ch2/{name}'")  # For lightboxes that passed bare name earlier?
    # Also replace inside openLightbox('images/ch2-...' with openLightbox('images/ch2/ch2-...'
    html = html.replace(f"openLightbox('images/{name}'", f"openLightbox('images/ch2/{name}'")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('HTML updated.')
