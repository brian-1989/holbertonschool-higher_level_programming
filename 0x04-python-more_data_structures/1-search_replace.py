#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(0, len(my_list)):
        # add the elements to the new list
        new_list.append(my_list[i])
        # condicition to search the coincidence and replace
        if my_list[i] == search:
            new_list[i] = replace
    return new_list
