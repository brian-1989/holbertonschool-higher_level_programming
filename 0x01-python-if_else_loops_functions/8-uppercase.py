#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        # condiction to check if j is lower
        if j >= 97 and j <= 122:
            j = ord(i) - 32
        else:
            j = ord(i)
        print("{}".format(chr(j)), end="")
    print(end="\n")
