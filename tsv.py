#!/usr/bin/env python2.7
# tsv.py: a module for writing TSV (tab-separated value) files
"""
This module defines two classes: a TsvWriter, which can be constructed on a
stream to allow writing TSV data lines and #-delimited comments to that stream,
and a TsvReader, which can be constructed on a stream and iterated over to
obtain lists of the values from each non-comment line in the stream.

TSV is most useful as the basis for other, more tightly specified file formats.

Examples of how to use this module are available here:
https://github.com/adamnovak/tsv/blob/master/README.md

"""

class TsvWriter(object):
    """
    Represents a writer for tab-separated value files containing  #-delimited
    comments.
    
    """
    def __init__(self, stream):
        """
        Make a new TsvWriter for writing TSV data to the given stream.
        """
        
        # This holds the stream
        self.stream = stream
    
    
    def line(self, *args):
        """
        Write the given values to the file, as a TSV line. Args holds a list of
        all arguments passed. Any argument that stringifies to a string legal as
        a TSV data item can be written.
        
        """
        
        self.list_line(args)
        
    
    def list_line(self, line):
        """
        Write the given iterable of values (line) to the file as items on the 
        same line. Any argument that stringifies to a string legal as a TSV data
        item can be written.
        
        Does not copy the line or build a big string in memory.
        """
        
        if len(line) == 0:
            return
        
        self.stream.write(str(line[0]))
        
        for item in line[1:]:
            self.stream.write("\t")
            self.stream.write(str(item))
        
        self.stream.write("\n")
        
    def comment(self, text):
        """
        Write the given text as a TSV comment. text must be a string containing
        no newlines.
        
        """
        
        self.stream.write("# {}\n".format(text))
        
    def close(self):
        """
        Close the underlying stream.
        """
        
        self.stream.close()
        
class TsvReader(object):
    """
    Represents a reader for tab-separated value files. Skips over comments 
    starting with #. Can be iterated over.
    
    Field values consisting of only whitespace are not allowed.
    """
    
    def __init__(self, stream):
        """
        Make a new TsvReader to read from the given stream.
        """
        
        self.stream = stream
        
    def __iter__(self):
        """
        Yields lists of all fields on each line, as strings, until all lines are
        exhausted. Strips whitespace around field contents. 
        """
        
        for line in self.stream:
            line = line.strip()
            if line == "" or line[0] == "#":
                # Skip comments and empty lines
                continue
            
            yield map(str.strip, line.split("\t"))
            
    def close(self):
        """
        Close the underlying stream.
        """
        
        self.stream.close()
