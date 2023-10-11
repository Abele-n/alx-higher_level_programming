#!/usr/bin/python3
"""a save_to_json_file function definition"""
import json


def save_to_json_file(my_obj, filename):
    """return python object representation of a json string

    Args:
        my_obj(object): python object to be saved in json file
        filename(str): name of file where object is saved
    """
    return json.loads(my_obj)
