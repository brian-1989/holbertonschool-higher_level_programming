#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # travel the list with the range of argument (x)
    for j in range(0, x):
        try:
            # with this condition we make the exception
            if my_list[j] == x:
                print("{}".format(my_list[j]))
                return my_list[j]
            else:
                print("{}".format(my_list[j]), end="")
        # exception for when occurrence the error
        except IndexError:
            pass
    print(end="\n")
    return my_list[-1]
