#!/usr/bin/python3
""" This module contains the definition of a class named Square """


class Square:
    """This represents a class called Square."""
    def __init__(self, size=0):
    """initializes a new square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
