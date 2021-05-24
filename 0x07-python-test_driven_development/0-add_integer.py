#!/usr/bin/python3
"""
Sum
"""


def add_integer(a, b=98):
    """Function that sum two number.
    Return the total sum of two number.

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
