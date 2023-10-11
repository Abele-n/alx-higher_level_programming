#!/usr/bin/python3
"""python class_to_json definition"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure (list, di\
        ctionary, string, integer and boolean) for JSON serialization of an ob\
        ject"""
    return obj.__dict__
