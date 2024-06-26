#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Blue-print for a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of
           a Student instance (same as 8-class_to_json.py)
        """
        return self.__dict__
