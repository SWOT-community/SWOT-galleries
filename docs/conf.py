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
    'nbsphinx',
    'sphinx.ext.mathjax',
    # 'sphinx_gallery.gen_gallery',
]

# -- Extension configuration -------------------------------------------------
# sphinx_gallery_conf = dict(
#     # It is important to follow the auto_* convention, because the gitlab CI
#     # pipeline uses it to retrieve the notebook executions.
#     examples_dirs=['../dummy'],
#     gallery_dirs=['auto/dummy'],
#     filename_pattern=r'[\\\/]ex_',
#     only_warn_on_example_error=True,
#     remove_config_comments=True,
#     nested_sections=False,
#     # Do not inspect global variables in code blocks. The links are useful but
#     # their styling makes them too overwhelming
#     inspect_global_variables=False,
#     # ignore_repr_types=r'*DynamicMap*'
# )

# Don't add .txt suffix to source files:
html_sourcelink_suffix = ''

# This is processed by Jinja2 and inserted before each notebook
nbsphinx_prolog = r"""
{% set docname = 'doc/' + env.doc2path(env.docname, base=None) %}

.. raw:: html

    <div class="admonition note">
      <a href="{{ env.docname.split('/')|last|e + '.ipynb' }}" class="reference download internal" download>Download notebook</a>.
    </div>
"""

nbsphinx_epilog = nbsphinx_prolog

nbsphinx_thumbnails = {
  'CNES-AVISO/ex_aviso_download_swot': '_images/aviso.png',
  'SWOT-Hydrology/BASIC/Hydrocron_SWOT_timeseries_examples': '_static/Hydrocron_logo.png',
  'SWOT-Hydrology/BASIC/Search_by_earthaccess_python_package': '_static/earthaccess_logo.png',
  'SWOT-Hydrology/BASIC/Search_by_SWORD_River_ID_in_Earthdata': '_static/SWORD_River_reaches.png',
  'SWOT-Hydrology/BASIC/SWOT_Raster_Notebook_cloud_in_Earthdata': '_static/Raster_QF_example.png',
  'SWOT-Hydrology/BASIC/SWOT_Raster_Notebook_local_in_Earthdata': '_static/Raster_QF_example.png',
  'SWOT-Hydrology/INTERMEDIATE/download_pixc_to_zarr': '_static/zarr.png',
  'SWOT-Hydrology/INTERMEDIATE/download_pixc_to_gpkg': '_static/geopkg.png',
}


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

