#!/usr/bin/python3
"""
function is same class
"""


def is_same_class(obj, a_class):
    """function that compare if the object is exactly an instance
    of the specified class.
    args:
        obj: object to compare.
        a_class: specified class.
    Return true if the object is the specified class and false, if not is.

    """
    if type(obj) is a_class:
        return True
    else:
        return False
