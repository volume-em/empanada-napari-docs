# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'empanada-napari-v1.2'
copyright = '2026 Allan Almeida,  Abhishek Bhardwaj, Kedar Narayan ,Madeline Barry, Mariam Demir and Ryan Conrad'
author = 'Allan Almeida'
release = '1.2.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.napoleon',
	'sphinx.ext.viewcode',
	'sphinx.ext.autosummary',
	'sphinx.ext.autosectionlabel',
	"sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
	"primary_sidebar_end": ["indices.html", "sidebar-ethical-ads.html"],
	"show_nav_level": 0,
	"announcement": "<b>empanada-napari v1.2.4 is now available! New models for mitochondria, nuclei, and lipid droplets. Update <a href='https://empanada.readthedocs.io/en/latest/getting_started/install.html'>here!</a></b>",
}
html_logo = '_static/empanada_logo_icon.png'
html_favicon = '_static/favicon.ico'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
