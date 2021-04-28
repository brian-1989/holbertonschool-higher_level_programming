#!/usr/bin/python3
for i in range(0, 100):
    # condition to the last digit and set the line jump
    if i == 99:
        print(i)
        break
    # 0:02d, zero is added at position 2
    print("{0:02d}".format(i), end=", ")
