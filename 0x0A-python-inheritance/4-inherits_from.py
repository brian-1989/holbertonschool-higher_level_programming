#!/usr/bin/python3
"""
function inherits from
"""


def inherits_from(obj, a_class):
    """function that compare if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    args:
        obj: object to compare.
        a_class: specified class.
    Return true if the object is a instance inherited (directly or indirectly)
    and false, if not is.

    """
    if type(obj) is not a_class:
        if isinstance(obj, a_class):
            return True
        else:
            return False
    else:
        return False
