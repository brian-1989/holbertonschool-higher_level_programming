#!/usr/bin/python3
# -1, to print the alphabet in reverse order
for i in range(122, 96, -1):
    # condition to alternating lowercase and uppercase
    if i % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end="")
