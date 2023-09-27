#!/usr/bin/python3
"""class Square definition"""


class Square:
    """a class representing a square"""
    def __init__(def, size=0):
        """a new square initialization

        Args:
        size(int): the new square size
        """

        self.size = size

        @property
        def size(self):
            """Get current size of square"""
            return (self.__size)

        @size.setter

        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """Gets the current area of the square"""
                return (self.__size * self.__size)
