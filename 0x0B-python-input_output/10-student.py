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
        """retrieves a dictionary representation of a Student
           instance (same as 8-class_to_json.py):
        """
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
        else:
            return self.__dict__

