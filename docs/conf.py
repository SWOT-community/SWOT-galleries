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


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
