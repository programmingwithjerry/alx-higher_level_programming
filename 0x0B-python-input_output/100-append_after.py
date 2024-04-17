#!/usr/bin/python3
"""Defines a function to insert text into a text file."""

def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a specific string"""
    updated_text = ""
    with open(filename) as file_read:
        line = file_read.readline()
        while line:
            updated_text += line
            if search_string in line:
                updated_text += new_string
            line = file_read.readline()
    with open(filename, "w") as file_write:
        file_write.write(updated_text)

