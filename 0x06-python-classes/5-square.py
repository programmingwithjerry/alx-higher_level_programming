#!/usr/bin/python3
"""This module contains the definition of an empty class named 'Square.' """


class Square:
    """This Represents a square."""
    def __init__(self, size=0):
        """Initializes a new square."""
        self.size = size

    @property
    def size(self):
        """This Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """This Sets the value of the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints onto stdout the square with the character #."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
