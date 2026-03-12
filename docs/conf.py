# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SWOT Gallery'
copyright = '2024, SWOT Community'
author = 'SWOT Community'
release = '0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    "sphinx_design",
    'sphinx.ext.mathjax',
    'sphinx_tabs.tabs',
]

# Don't add .txt suffix to source files:
html_sourcelink_suffix = ''

nb_execution_mode = "off"
nb_execution_timeout = 120
nb_execution_allow_errors = False

templates_path = ['_templates']
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'pydata_sphinx_theme'
#html_theme = 'alabaster'


# Title
html_title = "SWOT Community"
html_short_title = "SWOT Community"

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["css/custom.css"]


# Logo
html_logo = "_static/SWOT_spacecraft_model.png"

# Favicon
html_favicon = "_static/swot_favicon.png"

# Theme options
html_theme_options = {
    "logo_only": True,
    "navigation_depth": 4,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

import subprocess
from pathlib import Path

def generate_thumbnails(app):

    script = Path(__file__).parent / "scripts" / "generate_thumbnails.py"
    subprocess.run(["python", str(script)])

def insert_links(app):
    script = Path(__file__).parent / "scripts" / "insert_download_links.py"
    subprocess.run(["python", str(script)])

def setup(app):
    app.connect("builder-inited", generate_thumbnails)
    app.connect("builder-inited", insert_links)