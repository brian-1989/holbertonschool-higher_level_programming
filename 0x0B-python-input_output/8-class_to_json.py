#!/usr/bin/python3
"""
Object to serialization.
"""


def class_to_json(obj):
    """functionthat describes a dictionary for JSON serialization
    of an object.
    Arg:
        obj: object to serialization.
    Return the dictionary description with simple data structure.

    """
    return obj.__dict__