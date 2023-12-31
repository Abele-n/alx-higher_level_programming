#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """computation of the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value validation method"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
