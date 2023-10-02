#!/usr/bin/python3
"""Defining the class Rectangle"""


class Rectangle:
    """Representing the class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the new rectangle

        Args:
        width(int): the new rectangle width
        height(int): the new rectangle height
        """

        self.height = height
        self.width = width

        @property
        def height(self):
            """sets the height of the rectangle"""
            return self._height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value

        @property
        def width(self):
            """sets the width of the rectangle"""
            return self._width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value

            def perimeter(self):
                """Returns the perimeter of the rectangle"""
                if self._height == 0 or self._width == 0:
                    return (0)
                else:
                    return ((2 * self._height) + (2 * self._width))

                def area(self):
                    """Returns the area of the rectangle"""
                    return (self._height * self._width)
