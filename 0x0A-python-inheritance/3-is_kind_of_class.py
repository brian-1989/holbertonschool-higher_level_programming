#!/usr/bin/python3
"""
function is kind of class
"""


def is_kind_of_class(obj, a_class):
    """function that compare if the object is exactly an instance
    of the specified class or if the object is an instance of a class
    that inherited.
    args:
        obj: object to compare.
        a_class: specified class.
    Return true if the object is the specified class or an instance
    of class that inherited and false, if not is.

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
