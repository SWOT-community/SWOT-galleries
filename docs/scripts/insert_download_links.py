import glob, os, nbformat

def main():
    pattern = "docs/SWOT-Oceanography/*.ipynb"
    for fn in glob.glob(pattern):
        nb = nbformat.read(fn, as_version=4)
        basename = os.path.basename(fn)
        link = f"[Download notebook]({basename})"
        cell = nbformat.v4.new_markdown_cell(link)
        
        if not any(c.cell_type=="markdown" and c.source==link for c in nb.cells):
            nb.cells.insert(0, cell)
            nb.cells.append(cell)
            nbformat.write(nb, fn)

if __name__=="__main__":
    main()