#!/usr/bin/python3
"""
Square
"""


def print_square(size):
    """Function that print a square with a size specified.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        if i < size:
            print(end="\n")
