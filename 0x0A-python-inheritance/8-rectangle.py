#!/usr/bin/python3
"""Rectangle class module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """subclass representing the rectangle"""
    def __init__(self, width, height):
        """the constructors"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
