#!/usr/bin/python3
"""A module containing a rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Serves as a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the object"""
        super().__init__(id)
        
        # Assign each argument width, height, x, and y to the right attribute
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with the character '#'"""
        for _ in range(self.y):
            print()  # Move cursor down to the specified y position
        
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
