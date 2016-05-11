import os
import fnmatch

def findAvida():
    dirname = ""
    for dir in os.listdir('..'):
        if fnmatch.fnmatch(dir, '*avida*'):
            dirname = dir
            print "Found Avida directory: ", dirname

