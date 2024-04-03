#!/usr/bin/python3
""" This module contains the definition of a class named Square """

class Square:
    """This represent Square class"""
    def __init__(self, size=0):
	"""initializes a new square.
        Arguments include:
        size(int)=0: the optional size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
