#!/usr/bin/python3
for i in range(97, 123):
    # condition to not print the vocal e or q
    if i == 101 or i == 113:
        continue
    # chr return a character, as would be in ASCII code
    print("{}".format(chr(i)), end="")
    # delete the line jump
