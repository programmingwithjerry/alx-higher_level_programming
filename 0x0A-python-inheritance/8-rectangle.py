#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""A module with just one class - Rectangle
  that inherits from BaseGeometry (7-base_geometry.py)."""


class Rectangle(BaseGeometry):
    """class Rectangle, inherited from class
    BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
