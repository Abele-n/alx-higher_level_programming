#!/usr/bin/python3
"""The lookup function method"""


def lookup(obj):
    """returns all properties and methods of lookup obj

    Args:
    obj (object): object in the list

    Return:
    Methods and properties of obj
    """

    return dir(obj)
