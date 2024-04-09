#!/usr/bin/python3
"""
Module that Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)"""
    # Validate m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    # Validate m_a is not empty
    if not m_a or not all(isinstance(row, list) for row in m_a):
        raise ValueError("m_a can't be empty and must be a list of lists")

    # Validate m_b is not empty
    if not m_b or not all(isinstance(row, list) for row in m_b):
        raise ValueError("m_b can't be empty and must be a list of lists")

    # Validate each row of m_a has the same size
    l1 = len(m_a)
    l2 = len(m_a[0])  # Size of first row of m_a
    if any(len(row) != l2 for row in m_a):
        raise TypeError("each row of m_a must have the same size")

    # Validate each row of m_b has the same size
    l3 = len(m_b[0])  # Size of first row of m_b
    if any(len(row) != l3 for row in m_b):
        raise TypeError("each row of m_b must have the same size")

    # Validate m_a and m_b can be multiplied
    if l2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Validate elements of m_a and m_b are integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Multiply matrices
    result = []
    for i in range(l1):
        row = []
        for j in range(l3):
            n = 0
            for k in range(l2):
                n += m_a[i][k] * m_b[k][j]
            row.append(n)
        result.append(row)
    return result

