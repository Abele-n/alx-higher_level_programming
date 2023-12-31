#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """Representing the class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes my new rectangle

        Args:
        width(int): my new rectangle width
        height(int): my new rectangle height
        """
        self.height = height
        self.width = width

        @property
        def width(self):
            """returns the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """returns the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
