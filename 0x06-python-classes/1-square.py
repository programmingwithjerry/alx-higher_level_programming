#!/usr/bin/python3
"""Defines a class Square by private"""


class Square:
    """ The Square class."""
    def __init__(self, size):
        """Initializes a new square.
        Args:
        size(int): size of a new square.
        """
        self.__size = size
