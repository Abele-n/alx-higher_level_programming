#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """uniquely specialised MyList class"""
    def print_sorted(self):
        """prints the sorted self"""
        print(sorted(self))
