#!/usr/bin/python3
""" Defines a class LockedClass """


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes
    """
    __slots__ = ['first_name']
