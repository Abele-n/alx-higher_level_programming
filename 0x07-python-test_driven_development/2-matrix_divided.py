#!/usr/bin/python3
"""Defining the matrix division function"""


def matrix_divided(matrix, div):
    """all elements of a matrix are divided

    Args:
    div(float/int): the divisor element
    matrix(list): the list of float or int floats
    Raises:
    TypeError: the matrix contains non-numbers
    TypeError: Matrix contains rows of different sizes
    TypeError: if the div is neither a float nor int
    ZeroDivisionError: if div is 0
    Returns:
    result of matrix division
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix) or not all(isinstance(elem, int) or isinstance(elem, float)) for elem in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
