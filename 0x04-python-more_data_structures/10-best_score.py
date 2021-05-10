#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    # take out the values of the dictionary
    values = a_dictionary.values()
    # enter the dictionary values on a list
    list_values = list(values)
    list_values.sort()
    # maximum dictionary value
    max_value = list_values[-1]
    for i, j in a_dictionary.items():
        # condition to compare values with the maximum dictionary value
        if j == max_value:
            return i
