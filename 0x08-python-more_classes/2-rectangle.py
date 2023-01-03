#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Depicts a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises a new rectangle instance

        Args:
            width (int): The width of the rectangle
            height(int): The height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets/Sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/Sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
