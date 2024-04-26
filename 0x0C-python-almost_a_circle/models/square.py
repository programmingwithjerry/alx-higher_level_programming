#!/usr/bin/python3
"""Module containing a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Serves as a square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Sets a format for the string representation of this class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Getter for the size property"""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter for the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates/assigns attributes of an instance"""
        if args and len(args) > 0:
            if args[0] is not None:
                if not isinstance(args[0], int):
                    raise TypeError("id must be an integer")
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None and not isinstance(value, int):
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
