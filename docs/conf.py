# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import subprocess
import sys
from pathlib import Path

# -- Path setup ---------------------------------------------------------------

SCRIPTS_PATH = Path(__file__).parent / "scripts"
sys.path.insert(0, str(SCRIPTS_PATH))

# -- Project information ------------------------------------------------------

project = 'SWOT Gallery'
copyright = '2024, SWOT Community'
author = 'SWOT Community'
release = '1.0'

# -- General configuration ----------------------------------------------------

extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx.ext.mathjax",
    "sphinx_tabs.tabs",
]

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"

# -- MyST configuration -------------------------------------------------------

myst_enable_extensions = ["substitution"]

from generate_versions import get_myst_substitutions
myst_substitutions = get_myst_substitutions()

# -- Notebook execution -------------------------------------------------------

nb_execution_mode = "off"
nb_execution_timeout = 120
nb_execution_allow_errors = False

# -- HTML output --------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_title = "SWOT Community"
html_short_title = "SWOT Community"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_logo = "_static/SWOT_spacecraft_model.png"
html_favicon = "_static/swot_favicon.png"
html_sourcelink_suffix = ''

html_theme_options = {
    "logo_only": True,
    "navigation_depth": 4,
}

# -- Build hooks --------------------------------------------------------------

def setup(app):
    app.connect("builder-inited", lambda app: subprocess.run(
        ["python", str(SCRIPTS_PATH / "generate_thumbnails.py")]
    ))
    app.connect("builder-inited", lambda app: subprocess.run(
        ["python", str(SCRIPTS_PATH / "insert_download_links.py")]
    ))