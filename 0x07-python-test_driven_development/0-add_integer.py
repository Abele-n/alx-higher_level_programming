#!/usr/bin/python3
"""Degining an addition integer function"""


def add_integer(a, b=98):
    """Gets the addition integer of a and b

    a and b must be first casted to integers if they are float

    raises:
    TypeError: If either a or b is non-float and non-integer
    """

    if (not isinstance(a, float) and not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
