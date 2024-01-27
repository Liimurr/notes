# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Example'
copyright = 'workshop participant'
author = 'workshop participant'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'myst_parser',
  'sphinx_design',
  'nbsphinx',
  'sphinx_tabs.tabs',
  # 'sphinx_copybutton',
  'sphinx.ext.graphviz',

  # Themes
  # ======
  'sphinxawesome_theme',
  'sphinxawesome_theme.highlighting'
]
source_suffix = [".rst", ".md"]
myst_enable_extensions = ["colon_fence"]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
graphviz_output_format = 'svg'
pygments_style = 'github-light-high-contrast'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
from dataclasses import asdict
from sphinxawesome_theme import ThemeOptions
html_theme = 'sphinxawesome_theme'

# https://sphinxawesome.xyz/how-to/configure/#sphinxawesome_theme.ThemeOptions
theme_options = ThemeOptions(show_nav=False)

html_logo = "_static/logo.png"
html_static_path = ['_static']  