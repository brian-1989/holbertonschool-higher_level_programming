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
    peak_list = []
    _len = len(list_of_integers) - 1
    if list_of_integers[0] >= list_of_integers[1]:
        peak_list.append(list_of_integers[0])
    if list_of_integers[_len] >= list_of_integers[_len - 1]:
        peak_list.append(list_of_integers[_len])
    for i in range(2, _len):
        if list_of_integers[i] >= list_of_integers[i - 1] and\
                list_of_integers[i] >= list_of_integers[i + 1]:
            peak = list_of_integers[i]
            peak_list.append(peak)
    if len(peak_list) == 1:
        return peak_list[0]
    else:
        peak_list.sort()
        return peak_list[-1]
