#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j >= 65 and j <= 90 or j == 32 or j >= 48 and j <= 57:
            j = ord(i)
        else:
            j = ord(i) - 32
        print("{}".format(chr(j)), end="")
    print(end="\n")
