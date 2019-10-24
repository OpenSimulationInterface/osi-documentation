# -*- coding: utf-8 -*-
#
import os
import sys
import sphinxcontrib.spelling
import textwrap
# sys.path.insert(0, os.path.abspath('.'))
sys.path.append('/home/travis/build/OpenSimulationInterface/osi-documentation/osi-validation')
sys.path.append('/home/travis/build/OpenSimulationInterface/osi-documentation/breathe')

# -- Project information -----------------------------------------------------

project = 'Open Simulation Interface'
copyright = '2019, Carlo van Driesten'
author = 'Carlo van Driesten'

# The short X.Y version
# version = ''
# The full version, including alpha/beta/rc tags
release = 'v3.1.2'

add_module_names = False

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.spelling',
    'breathe',
    'exhale',
    'recommonmark'
]
breathe_projects = { "open-simulation-interface": "/home/travis/build/OpenSimulationInterface/osi-documentation/osi-validation/open-simulation-interface/doc/xml" }
breathe_default_project = "open-simulation-interface"

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./open-simulation-interface/doc",
    "rootFileName":          "library_root.rst",
    "rootFileTitle":         "OSI Reference",
    "doxygenStripFromPath":  "..",
    # Suggested optional arguments
    "createTreeView":        True,
    "afterTitleDescription": textwrap.dedent('''
    .. WARNING::

       Currently this reference is **work in progress** to port the doxygen 
       documentation completely to the sphinx documentation. 
       For the official reference see the current 
       `OSI reference documentation <https://opensimulationinterface.github.io/open-simulation-interface/annotated.html>`_.
    ''')
}


# Show spelling suggestions
spelling_show_suggestions = True
spelling_word_list_filename = ['spelling/spelling_wordlist.txt', 
                               'spelling/abbreviations.txt',
                               'spelling/file_endings.txt',
                               'spelling/human_names.txt',
                               'spelling/general_names.txt',
                               'spelling/file_names.txt',
                               'spelling/function_names.txt']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 
                    'Thumbs.db', 
                    '.DS_Store', 
                    'vpython', 
                    '.github',
                    'osi-validation/open-simulation-interface',
                    'osi-validation/proto2cpp',
                    'osi-validation/.github',
                    'osi-sensor-model-packaging/.github',
                    'open-simulation-interface/.github',
                    'osi-visualizer/.github',
                    'proto2cpp/.github',
                    'breathe/*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
# html_theme = "default"
html_theme = "sphinx_rtd_theme"

# import sphinx_glpi_theme

# html_theme = "glpi"
# html_theme_path = sphinx_glpi_theme.get_html_themes_path()
