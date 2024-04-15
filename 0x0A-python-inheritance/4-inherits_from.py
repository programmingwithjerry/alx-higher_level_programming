#!/usr/bin/python3
"""module with one method - inherits_from."""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
       (directly or indirectly) from the specified class ; otherwise False."""
    mro = type(obj).__mro__
    return a_class in mro and a_class != type(obj)
