#!/usr/bin/python3
"""string-to-json function definition"""
import json


def to_json_string(my_obj):
    """Gets the representation of json in string form"""
    return json.dumps(my_obj)
