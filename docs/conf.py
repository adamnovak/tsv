# -*- coding: utf-8 -*-
#

# Sphinx configuration
# Cribbed from <https://github.com/ondrejsika/sphinx-autodoc-example>

import sys
import os

sys.path.insert(0, os.path.abspath('../src/'))

extensions = ['sphinx.ext.autodoc']
source_suffix = '.rst'
master_doc = 'index'
project = u'tsv'
copyright = u'Adam Novak, anovak@soe.ucsc.edu'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
autoclass_content = 'both'
