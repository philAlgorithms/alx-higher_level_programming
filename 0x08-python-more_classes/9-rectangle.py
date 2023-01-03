#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Depicts a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances
        print_symbol (any): The charactor for representing rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area

        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        Raises:
            TypeError: if either of the parameters is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle with equal width and height

        Args:
            size (int): The size of the width ad height
        """
        return (cls(size, size))

    def __str__(self):
        """Returns a printable depiction of the rectabgle

        Depicts the rectangle as a clock of # characters
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        r = []
        for i in range(self.__height):
            [r.append(str(self.print_symbol)) for j in range(self.__width)]
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
