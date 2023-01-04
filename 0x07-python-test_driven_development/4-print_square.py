#!/usr/bin/python3
# 4-print_square.py
"""Defines a square printer"""

def print_square(size):
    """Prints a square of size 'size'

    Args:
        size (int): length of square.

    Raises:
        TypeError: if size is not integer
        ValueError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
