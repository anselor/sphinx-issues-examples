#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.intersphinx',
              'sphinx.ext.doctest',
              'sphinx.ext.todo']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'typevar'
copyright = '2020, Contributors'
author = 'contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# version will look like x.y.z
version = '0.0.1'
# release will look like x.y
release = '.'.join(version.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# configure autosectionlabel extension
autosectionlabel_prefix_document = True

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Custom theme from ReadTheDocs
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'hellodoc'


# -- Options for LaTeX output --------------------------------------------------



# -- Options for manual page output ---------------------------------------


# -- Options for Texinfo output -------------------------------------------


# -- Options for Extensions  -------------------------------------------
# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/3': None}

# options for autodoc
autodoc_default_options = {
    'member-order': 'bysource',
    'special-members': '__init__',
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}
autodoc_typehints = 'signature'
autoclass_content = 'both'

# Ignore nitpicky warnings from autodoc which are occurring for very new versions of Sphinx and autodoc
# They seem to be happening because autodoc is now trying to add hyperlinks to docs for typehint classes
nitpick_ignore = [
]


# def skip(app, what, name, obj, would_skip, options):
#     if name == '__init__':
#         return False
#     return would_skip
#
#
# def setup(app):
#     app.connect('autodoc-skip-member', skip)