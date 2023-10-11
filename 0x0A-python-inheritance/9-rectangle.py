#!/usr/bin/python3
"""Rectangle class module"""
BaseGeometry = __import__("7-base_geometry").BaseGeeometry


class Rectangle(BaseGeometry):
    """subclass representing a rectangle

    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    """
    def __init__(self, width, height):
        """the constructor"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """it calculatrs the area of the rectangle

        Returns:
            area(int): area of tje rectangle
        """
        return self.__height * self.__width
    def __str__(self):
        """
        Returns the description of the rectangle

        Returns:
            str: the rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
