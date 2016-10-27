# Configure Sphinx for ReadTheDocs
# From the ReadTheDocs getting started guide:
from recommonmark.parser import CommonMarkParser

source_parsers = {'.md': CommonMarkParser}
    
source_suffix = ['.rst', '.md']
