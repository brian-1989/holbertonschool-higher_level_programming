#!/usr/bin/python3
"""
Write a object.
"""


import json


def save_to_json_file(my_obj, filename):
    """function that wirte a objecto, using JSON.
    Args:
        my_obj: type of data to serialize.
        filename: name of file.

    """
    with open(filename, 'w') as text:
        json.dump(my_obj, text)
