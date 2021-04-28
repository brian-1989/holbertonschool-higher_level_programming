#!/usr/bin/python3
for i in range(0, 10):
    # increase the value of I, one unit
    j = i + 1
    for j in range(j, 10):
        # condition to the last number, set the line jump
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
            break
        print("{}{}".format(i, j), end=", ")
