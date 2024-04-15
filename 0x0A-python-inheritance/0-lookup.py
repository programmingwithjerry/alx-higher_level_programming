#!/usr/bin/python3
"""module with one funaction named lookup
"""


def lookup(obj):
    """returns the list of available attributes and
       methods of an object
    """
    return (list(dir(obj)))
