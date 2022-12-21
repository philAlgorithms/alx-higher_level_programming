#!/usr/bin/python3

"""Defines a square class"""


class Square:
    """Represents a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance

        Args:
            size (int): The size of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of the square"""
        return self.__position

    @position.setter
    def position(self, val):
        if (not isinstance(val, tuple) or
                len(val) != 2 or
                not all(isinstance(num, int) for num in val) or
                not all(number >= 0 for number in val)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
