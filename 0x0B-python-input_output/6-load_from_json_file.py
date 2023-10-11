#!/usr/bin/python3
"""json file-reafing function defination"""
import json


def load_from_json_file(filename):
    """creates python object from the json file"""
    with open(filename) as f:
        return json.load(f)
