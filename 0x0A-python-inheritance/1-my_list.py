#!/usr/bin/python3
"""
    A Module with one class MyList
"""


class MyList(list):
    """Class MyList that inherits from list"""
    pass

    def print_sorted(self):
        """Method that prints the list, but sorted (ascending sort)"""

        print(sorted(list(self)))
