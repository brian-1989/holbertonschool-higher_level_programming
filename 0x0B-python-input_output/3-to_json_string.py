#!/usr/bin/python3
"""
JSON object
"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object.
    Args:
        my_obj: argument to convert.
    Return the object type JSON.

    """
    return json.dumps(my_obj)
