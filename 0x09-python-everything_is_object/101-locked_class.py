#!/usr/bin/python3
"""Defining the class LockedClass"""


class LockedClass:
    """Representation of the class LockedClass"""
    __slots__ = ("first_name", )

    """initializing the first name"""
    def __init__(self, first_name):
        self.first_name = first_name