#!/usr/bin/python3
"""JSON file-writing function dsfinition"""
import json


def save_to_json_file(my_obj, filename):
    """writing an object to text fie using json representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
