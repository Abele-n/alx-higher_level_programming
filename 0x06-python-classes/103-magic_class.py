#!/usr/bin/python3
"""MagicClass definition matching bytecode"""


import math
class MagicClass:
    """a representation of a circle"""
    def __init__(self, radius=0):
        """MagicClass initialization

        Arg:
        radius(int or float): the new MagicClass radius
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
                raise TypeError("radius must be a number")
                self.__radius = radius

                def area(self):
                """Gets the area of MagicClass"""
                return (self.__radius ** 2 * math.pi)

                def circumference(self):
                """Gets the circumference of MagicClass"""
                return (2 * math.pi * self.__radius)
