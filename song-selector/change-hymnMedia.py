import json
from pathlib import Path

# Path to your single JSON file
file_path = Path("song-selector/Hymns.json")  # change to your file name

# Load the JSON
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Process each hymn
for hymn in data:
    if "HymnMedia" in hymn and isinstance(hymn["HymnMedia"], dict):
        # Wrap single object in a list
        hymn["HymnMedia"] = [hymn["HymnMedia"]]

# Save back to the same file (or use a backup path)
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done! HymnMedia updated where needed.")
