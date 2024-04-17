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
    """Get a dictionary representation of the Student.

    If attrs is a list of strings, represents only those attributes
    included in the list.

    Args:
        attrs (list): (Optional) The attributes to represent.
    """
    if type(attrs) == list and all(type(attr) == str for attr in attrs):
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
    return self.__dict__
 

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)


