# -*- coding: utf-8 -*-

extensions = [ "sphinx_rtd_theme"]

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'PHPCR'
copyright = u'2014, PHPCR contributors'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# This will be used when using the shorthand notation
highlight_language = 'php'

# enable highlighting for PHP code not between <?php ... ?> by default
lexers['php'] = PhpLexer(startinline=True)

# -- Options for HTML output ---------------------------------------------------

html_theme = "sphinx_rtd_theme"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/logo_small.png"

html_static_path = ['_static']
html_css_files = [
    'css/phpcr.css',
]
