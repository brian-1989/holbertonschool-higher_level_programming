#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_count = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            num_count += 1
        # add the errors occurred
        except (ValueError, TypeError):
            pass
    print(end="\n")
    return num_count
