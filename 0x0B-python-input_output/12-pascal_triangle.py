#!/usr/bin/python3
"""This module defines a Pascal's Triangle function - 
   generate_pascals_triangle
"""

def generate_pascals_triangle(n):
    """Returns a list of lists of integers
       representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle_rows = [[1]]
    while len(triangle_rows) != n:
        previous_row = triangle_rows[-1]
        new_row = [1]
        i = 0
        while i < len(previous_row) - 1:
            new_row.append(previous_row[i] + previous_row[i + 1])
            i += 1
        new_row.append(1)
        triangle_rows.append(new_row)
    return triangle_rows

