#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        # condicition to check if es module of two
        if i % 2 == 0:
            # add elements to the list
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
