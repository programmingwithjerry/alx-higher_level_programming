#!/usr/bin/python3
"""Create a Rectangle class."""


class Rectangle:
    """Defines a rectangle class.
    """
    def __init__(self, width=0, height=0):
        """Initializes Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Compute the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """:
            Compute the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Print the rectangle using eval."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print("Bye rectangle...")
