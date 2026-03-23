import re

with open('ch02.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Mapping old src string to the correct generated image
mapping = {
    'images/imperialism_cartoon.jpg': 'images/ch2-imperialism.jpg',
    'images/social_darwinism.jpg': 'images/ch2-imperialism.jpg', 
    'images/ww1_alliances.jpg': 'images/ch2-alliances.jpg',
    'images/balkan_powder_keg.jpg': 'images/ch2-alliances.jpg',
    'images/sarajevo.jpg': 'images/ch2-sarajevo.jpg',
    'images/trench.jpg': 'images/ch2-trench.jpg',
}

for old, new in mapping.items():
    # Replace src
    html = html.replace(f'src="{old}"', f'src="{new}"')

# Let's cleanly remove onerror attributes so they don't cause issues
html = re.sub(r' onerror="[^"]*"', '', html)

# Also fix the onclick openLightbox mapping
for old, new in mapping.items():
    html = html.replace(f"openLightbox('{old}'", f"openLightbox('{new}'")

with open('ch02.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Fixed images in ch02.html')
