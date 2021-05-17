#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_count = 0
    # travel the list with the range of argument (x)
    for j in range(0, x):
        try:
            # with this condition we make the exception
            print("{}".format(my_list[j]), end="")
            num_count += 1
        # exception for when occurrence the error
        except IndexError:
            pass
    print(end="\n")
    return num_count
