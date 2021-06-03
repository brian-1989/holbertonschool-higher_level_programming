#!/usr/bin/python3
"""
JSON deserialization
"""
import json


def from_json_string(my_str):
    """funcion that deserialization a string.
    Arg:
        my_str: string to deserialize
    Return an object (Python data structure) represented
    by a JSON string

    """
    return json.loads(my_str)
