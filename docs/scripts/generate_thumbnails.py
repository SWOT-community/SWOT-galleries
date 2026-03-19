import json
import base64
from pathlib import Path
from PIL import Image
from io import BytesIO

GALLERIES = [
    "Oceanography",
    "Hydrology",
]

def get_image_from_cell(cell):
    """Return PIL image if cell contains a PNG output."""
    for output in cell.get("outputs", []):
        data = output.get("data", {})
        if "image/png" in data:
            img_data = data["image/png"]

            # parfois stocké sous forme de liste
            if isinstance(img_data, list):
                img_data = "".join(img_data)

            img_bytes = base64.b64decode(img_data)
            return Image.open(BytesIO(img_bytes))

    return None


def extract_thumbnail(nb_path, thumb_path):
    with open(nb_path) as f:
        nb = json.load(f)

    thumbnail_cell = None
    fallback_cell = None

    for cell in nb["cells"]:

        tags = cell.get("metadata", {}).get("tags", [])
        if "thumbnail" in tags and thumbnail_cell is None:
            thumbnail_cell = cell

        if fallback_cell is None:
            if get_image_from_cell(cell) is not None:
                fallback_cell = cell

    target_cell = thumbnail_cell if thumbnail_cell else fallback_cell

    if target_cell:
        img = get_image_from_cell(target_cell)

        if img:
            img.thumbnail((400, 300))
            img.save(thumb_path)
            return True

    return False


def main():
    for gallery in GALLERIES:
        NOTEBOOK_DIR = Path(f"docs/SWOT-{gallery}")
        THUMB_DIR = Path("docs/_static/images/") / gallery.lower() / "_thumbs"
        THUMB_DIR.mkdir(parents=True, exist_ok=True)
        for nb in NOTEBOOK_DIR.rglob("*.ipynb"):
            thumb = THUMB_DIR / f"{nb.stem}.png"

            if not thumb.exists():
                extract_thumbnail(nb, thumb)


if __name__ == "__main__":
    main()