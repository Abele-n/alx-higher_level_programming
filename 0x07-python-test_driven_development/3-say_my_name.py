#!/usr/bin/python3
"""Defining the function name-print"""


def say_my_name(first_name, last_name=""):
    """prints the name

    Args:
    first_name: first name to print
    last_name: last name to print
    Raises:
    TypeError: if first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
