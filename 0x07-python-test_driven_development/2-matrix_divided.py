#!/usr/bin/python3
# 2-matrix_divided
"""Defines a function a matrix by a divisor"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div

    Raises:
        TypeError: if the matrix is not a list of lists
        TypeError: if number of elements of each row are not equal
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for a in matrix:
        if not isinstance(a, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for b in a:
            if not (isinstance(b, int) or isinstance(b, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    for a in matrix:
        if len(a) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
