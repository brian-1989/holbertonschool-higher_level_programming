#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for j in range(0, x):
        try:
            if my_list[j] == x:
                print("{}".format(my_list[j]))
                return my_list[j]
            else:
                print("{}".format(my_list[j]), end="")
        except IndexError:
            print(end="\n")
            return my_list[-1]
