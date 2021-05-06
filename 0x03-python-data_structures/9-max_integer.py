#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        # order the elements of the list of lower to greater
        my_list.sort()
        return my_list[-1]
