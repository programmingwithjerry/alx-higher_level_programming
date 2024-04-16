#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a
           Student instance (same as 8-class_to_json.py)
        """
        if attrs is not None:
            if hasattr(attrs, '__iter__') and all(isinstance(attr, str) for attr in attrs):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            else:
                return self.__dict__
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)

