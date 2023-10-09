#!/usr/bin/python3
"""a function that adds a new attribute to an object"""


def add_attribute(obj, attr, value):
    """function that adds new attribute

    Args:
    attr(string): attribute name to add to obj
    obj(: object to add an attribute
    value: attribute value
    Raises:
    TypeError: if new attribute can't be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
