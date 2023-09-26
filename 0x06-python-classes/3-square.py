#!/usr/bin/python3
"""class Square definition"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """new Square initialization

        Args:
        size(int): the new square size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """Gets the current area of the square"""
            return (self.__size * self.__size)
