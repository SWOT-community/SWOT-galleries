import glob
import os
import nbformat

GALLERIES = [
    "docs/SWOT-Oceanography",
    "docs/SWOT-Hydrology",
]

def process_notebook(fn):
    nb = nbformat.read(fn, as_version=4)
    basename = os.path.basename(fn)

    link = f"{{download}}`Download notebook <{basename}>`"
    cell = nbformat.v4.new_markdown_cell(link)

    if not any(c.cell_type == "markdown" and link in c.source for c in nb.cells):
        nb.cells.insert(0, cell)
        nb.cells.append(cell)
        nbformat.write(nb, fn)

def main():
    for gallery in GALLERIES:
        pattern = os.path.join(gallery, "**", "*.ipynb")
        for fn in glob.glob(pattern, recursive=True):
            process_notebook(fn)

if __name__ == "__main__":
    main()