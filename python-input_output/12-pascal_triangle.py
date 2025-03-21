#!/usr/bin/python3
"""
This module contains the implementation of Pascal's Triangle.
The module defines a function `pascal_triangle(n)` that generates
a list of lists of integers, representing the Pascal's Triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle as a list of lists of integers.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists, where each inner list represents a row
              in Pascal's Triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
    
    return triangle
