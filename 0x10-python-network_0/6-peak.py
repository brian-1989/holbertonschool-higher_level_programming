#!/usr/bin/python3
""" Find a peak.

"""


def find_peak(list_of_integers):
    """ Function that find a peak in a array.
    arg:
        lis_of_integers: array with the integers.

    """
    if list_of_integers == []:
        return
    list_of_integers.sort()
    return list_of_integers[-1]
