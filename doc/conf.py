# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Notes'
copyright = ''
author = 'Liam Murray'
release = '0.4.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.autosectionlabel',
  'myst_parser',
  'sphinx_design',
  'nbsphinx',
  'sphinx_tabs.tabs',
  'sphinx_copybutton',
  'sphinx.ext.graphviz',
  'hoverxref.extension'
]
source_suffix = [".rst", ".md"]
myst_enable_extensions = ["colon_fence"]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
graphviz_output_format = 'svg'
pygments_style = 'github-light-high-contrast'


html_theme = 'sphinx_book_theme'

# html_logo = "_static/logo.png"
html_static_path = ['_static']  
html_css_files = ['css/custom.css']
html_show_sphinx = False
