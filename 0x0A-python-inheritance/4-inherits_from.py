#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """is the object a true subclass of the class?"""
    return isinstance(obj, a_class) and type(obj) != class
