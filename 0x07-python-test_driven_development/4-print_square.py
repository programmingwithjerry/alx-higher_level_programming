#!/usr/bin/python3
"""
This is the "4-print_square" module with one function, print_square(size).
"""


def print_square(size):
    """Prints a square with '#'s that has a length of size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if size > 0:
        for _ in range(size):
            print("#" * size)
