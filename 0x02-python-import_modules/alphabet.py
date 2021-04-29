#!/usr/bin/python3
def uppercase(num_1, num_2):
    string = ""
    for i in range(num_1, num_2):
        string = string + chr(i)
    print("{}".format(string))
