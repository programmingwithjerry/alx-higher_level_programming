#!/usr/bin/python3
"""
Module with one class - MyList
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Returns the list of available
           attributes and methods of an object
        """

        print(sorted(list(self)))
