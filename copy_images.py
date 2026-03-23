import os
import shutil
import glob

brain_dir = r"c:\Users\grifo\.gemini\antigravity\brain\8848715a-8c12-4f7b-957c-58e257a0d7e9"
images_dir = r"c:\Users\grifo\OneDrive\AI\VibeVoding\CAI\LV9\images"

files = [
    ("map_asia_*.png", "map-asia.jpg"),
    ("imperialism_*.png", "ch2-imperialism.jpg"),
    ("alliances_*.png", "ch2-alliances.jpg"),
    ("sarajevo_*.png", "ch2-sarajevo.jpg"),
    ("trench_war_*.png", "ch2-trench.jpg"),
    ("submarine_*.png", "ch2-us-entry.jpg"),
    ("versailles_*.png", "ch2-versailles.jpg"),
    ("league_nations_*.png", "ch2-league.jpg"),
]

for pattern, new_name in files:
    matches = glob.glob(os.path.join(brain_dir, pattern))
    if matches:
        latest = max(matches, key=os.path.getctime)
        shutil.copy(latest, os.path.join(images_dir, new_name))
        print(f"Copied {latest} to {new_name}")

html_path = r"c:\Users\grifo\OneDrive\AI\VibeVoding\CAI\LV9\ch02.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    "https://via.placeholder.com/400x200?text=Imperialism": "images/ch2-imperialism.jpg",
    "https://via.placeholder.com/400x200?text=Alliances": "images/ch2-alliances.jpg",
    "https://via.placeholder.com/400x200?text=Sarajevo": "images/ch2-sarajevo.jpg",
    "https://via.placeholder.com/400x200?text=Trench+Warfare": "images/ch2-trench.jpg",
    "https://via.placeholder.com/400x200?text=US+Entry": "images/ch2-us-entry.jpg",
    "https://via.placeholder.com/400x200?text=Versailles": "images/ch2-versailles.jpg",
    "https://via.placeholder.com/400x200?text=League+of+Nations": "images/ch2-league.jpg"
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated ch02.html")
