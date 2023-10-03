#!/usr/bin/python3
"""Defining the print square function"""


def print_square(size):
    """prints a square with the character #

    Args:
    size(int): length of the square
    Raises:
    ValueError: size < 0
    TypeError: size is not an integer
    """

    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    for m in range(size):
        [print("#", end="") for n in range(size)]
        print("")
