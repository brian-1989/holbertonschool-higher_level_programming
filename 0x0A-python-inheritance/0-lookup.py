#!/usr/bin/python3
"""
function lookup
"""


def lookup(obj):
    """function that return the attributes and methods.
    Arg:
        obj: Get the class to return the attributes and methods.
    Return a list with the attributes and methods.

    """
    return dir(obj)
