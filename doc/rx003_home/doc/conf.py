# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import pathlib
import sys
import os

source_path = os.path.join(pathlib.Path(__file__).parents[1].resolve().as_posix(), "source")
sys.path.insert(0, os.path.abspath(source_path))

def check_builder(app):
    if app.builder.name == 'html':
        pass
    elif app.builder.name == 'latex':
        pass
    else:
        pass
    print(f"app.builder.name = {app.builder.name}")

def setup(app):
    app.connect('builder-inited', check_builder)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RX003 Home'
copyright = '2024, RX003'
author = 'RX003'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    'sphinxcontrib.bibtex',
    ]

templates_path = ['_templates']
exclude_patterns = [
    'technical_report/*.rst',
    'appendix/*.rst',
    '2024_0001_0007_template.rst'
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- OPtions for reference numbering
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-numfig

numfig = True
numfig_secnum_depth = (1)
numfig_format = {'figure': '그림 %s', 'table': '표 %s', 'code-block': ' 코드블록%s'}

# -- Options for LaTeX output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {
    # kotex config
    'fontpkg': r'''
\usepackage{kotex}

''',
}

bibtex_bibfiles = ['bibliography.bib']
