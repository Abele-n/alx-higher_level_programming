#!/usr/bin/python3
"""inherits_from module definition"""


def inherits_from(obj, a_class):
    """is the object a true subclass of the class?

    Args:
        obj: object to check
        a_class: specified class checking for inheritance
    Returns:
        True if the object is an instance of a class that inherited
        Otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != class
