#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # (^), this condition returns the elements that are not in both
    set_only = set_1 ^ set_2
    return set_only
