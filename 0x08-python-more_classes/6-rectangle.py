#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Depicts a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances
    """

    def __init__(self, width=0, height=0):
        """Initialises a new rectangle instance

        Args:
            width (int): The width of the rectangle
            height(int): The height of the rectangle
        """
        type(self).number_of_instances += 1
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

    def __str__(self):
        """Returns a printable depiction of the rectabgle

        Depicts the rectangle as a clock of # characters
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        r = []
        for i in range(self.__height):
            [r.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """Return a string representation of the rectangle """
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.height) + ")"
        return (r)

    def __del__(self):
        """Prints a message when an instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
