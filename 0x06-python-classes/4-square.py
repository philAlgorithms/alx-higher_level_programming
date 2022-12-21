#!/usr/bin/python3

"""Defines a square class"""


class Square:
    """Represents a square class"""

    def __init__(self, size=0):
        """Initializes a new Square instance

        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
