#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def is_it_peak(list_of_integers):
    """checks peak in an unsorted integer"""
    li = list_of_integers
    ln = len(li)
    if ln == 0:
        return None

    n = ln // 2
    if (n == ln - 1 or li[n] >= li[n + 1]) and (n == 0 or li[n] >= li[n - 1]):
        return li[n]

    if n != ln - 1 and li[n + 1] >= li[n]:
        return is_it_peak(li[n + 1:])

    return is_it_peak(li[:n])
