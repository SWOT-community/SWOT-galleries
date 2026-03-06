
import json
import base64
from pathlib import Path
from PIL import Image
from io import BytesIO

NOTEBOOK_DIR = Path("docs/SWOT-Oceanography")
THUMB_DIR = Path("docs/_static/thumbs")

THUMB_DIR.mkdir(parents=True, exist_ok=True)


def extract_thumbnail(nb_path, thumb_path):
    with open(nb_path) as f:
        nb = json.load(f)

    for cell in nb["cells"]:
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            if "image/png" in data:

                img_bytes = base64.b64decode(data["image/png"])
                img = Image.open(BytesIO(img_bytes))

                img.thumbnail((400, 300))
                img.save(thumb_path)

                return True

    return False


def main():
    for nb in NOTEBOOK_DIR.rglob("*.ipynb"):
        thumb = THUMB_DIR / f"{nb.stem}.png"

        if not thumb.exists():
            extract_thumbnail(nb, thumb)


if __name__ == "__main__":
    main()