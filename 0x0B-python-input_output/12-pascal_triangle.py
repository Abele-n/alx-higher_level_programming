#!/usr/bin/python3
"""Pascal's Triangle module definition"""


def pascal_triangle(n):
    """Pascal's triangle size n representation

    Returns:
    List of lists representing the triangle
    """

    if n <= 0:
        return []

    my_triangle = [[1]]
    while len(my_triangle) != n:
        triangle = my_triangle[-1]
        tmp = [1]
        for m in range(len(triangle) - 1):
            tmp.append(triangle[m] + triangle[m + 1])
        tmp.append(1)
        my_triangle.append(tmp)
    return my_triangle
