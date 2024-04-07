#!/usr/bin/python3
"""
    The "0-add_integer" module with one function, add_integer(a, b).
"""


def add_integer(a, b):
    """Return the addition of two numbers, a & b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    result = a + b
    return result
