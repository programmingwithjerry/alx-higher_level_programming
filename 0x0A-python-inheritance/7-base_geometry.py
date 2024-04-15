#!/usr/bin/python3
"""
module with class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """method for calculating area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating if a number is an integer"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

