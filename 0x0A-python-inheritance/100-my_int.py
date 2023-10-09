#!/usr/bin/python3
"""MyInt class definition"""


class MyInt(int):
    """integer as a rebel"""
    def __new__(cls, *args, **kwargs):
        """a new instance of the class is created"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __ne__(self, other):
        """converts == to !="""
        return int(self) == other

    def __eq__(self, other):
        """converts != to =="""
        return int(self) != other
