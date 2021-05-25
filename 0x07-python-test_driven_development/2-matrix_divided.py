#!/usr/bin/python3
"""
Division
"""


def matrix_divided(matrix, div):
    """Function that divide the lists with a number integer.
    Return an list with the elements divided by the integer.

    """
    new_list = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    for i in range(0, len(matrix)):
        my_list = []
        for j in range(0, len(matrix[i])):
            if not isinstance(matrix[i][j], int)\
                    and not isinstance(matrix[i][j], float):
                raise TypeError("\
matrix must be a matrix (list of lists) of integers/floats")
            a = "{:0.2f}".format(matrix[i][j] / div)
            my_list.append(float(a))
        new_list.append(my_list)
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    return new_list
