#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    sum = 0
    my_list = []
    new_list = []
    new_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    # this loop is to travel the chain of Roman numbers
    for k in roman_string:
        # This loop is to travel the dictionary that has the letters and
        # values, of the Roman numbers
        for i, j in new_dict.items():
            # condition to add the values of the letters found in roman_string
            if i == k:
                my_list.append(j)
                break
    # This loop runs through the stored values of the letters found,
    # in whole numbers
    for i in range(0, len(my_list)):
        # condition to validate if i is in the last position
        if i + 1 < len(my_list):
            # condition to validate the notation of the subtraction
            if my_list[i] >= my_list[i + 1]:
                new_list.append(my_list[i])
            else:
                new_list.append(my_list[i + 1] - my_list[i])
        else:
            if my_list[i] <= my_list[i - 1]:
                new_list.append(my_list[i])
            else:
                continue
    # this loop is to add the number of the list
    for i in new_list:
        sum += i
    return sum
