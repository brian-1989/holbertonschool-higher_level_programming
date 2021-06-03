#!/usr/bin/python3
"""
Read file JSON.
"""

import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”.
    Args:
        filename: name of file JSON.
    Return what's inside the JSON file.

    """
    with open(filename, 'r') as text:
        return json.loads(text.read())
