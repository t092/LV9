import shutil
import os

images = [
    'russian_revolution.jpg', 'lenin_speech.jpg', 'ussr_industry.jpg',
    'wall_street_crash.jpg', 'mussolini.jpg', 'hitler.jpg',
    'invasion_poland.jpg', 'pearl_harbor.jpg', 'normandy.jpg',
    'yalta_conference.jpg', 'un_logo.jpg'
]

# Using an existing image as placeholder
source = "images/img_21.jpeg"

if os.path.exists(source):
    for img in images:
        dest = os.path.join('images', img)
        shutil.copy(source, dest)
    print("Placeholder images copied successfully.")
else:
    print("Source image not found.")
