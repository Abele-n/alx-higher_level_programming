#!/usr/bin/python3
"""from_json_string module for working with json strings"""
import json


def from_json_string(my_str):
    """return python object representation of a json string

    Args:
        my_str(str): python string to be changed to json file
    """
    return json.loads(my_str)
