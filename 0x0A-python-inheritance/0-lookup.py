#!/usr/bin/python3
"""
Module with one class - MyList
"""


class MyList(list):
    """My list Class"""
    pass

    def print_sorted(self):
        """returns the list of available attributes and methods of an object"""

        print(sorted(list(self)))
