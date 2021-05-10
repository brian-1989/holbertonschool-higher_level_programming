#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i, j in a_dictionary.items():
        # add the elements to the new dictionary
        new_dictionary[i] = j * 2
    return new_dictionary
