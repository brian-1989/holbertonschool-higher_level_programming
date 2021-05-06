#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_2=()):
    _len_1 = len(tuple_a)
    _len_2 = len(tuple_2)
    if _len_1 < 2 or _len_2 < 2:
        # is concatenated with zeros, to the spaces that are empty
        tuple_a += (0, 0)
        tuple_2 += (0, 0)
        tu_to = (tuple_a[0] + tuple_2[0], tuple_a[1] + tuple_2[1])
        return tu_to
    else:
        tu_to = (tuple_a[0] + tuple_2[0], tuple_a[1] + tuple_2[1])
        return tu_to
