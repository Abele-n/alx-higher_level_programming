#!/usr/bin/python3
"""Rectangle class module"""
BaseGeometry = __import__("7-base_geometry").BaseGeeometry


class Rectangle(BaseGeometry):
    """subclass representing a rectangle"""
    def __init__(self, width, height):
        """the constructor"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
