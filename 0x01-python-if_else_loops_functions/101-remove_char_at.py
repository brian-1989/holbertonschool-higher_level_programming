#!/usr/bin/python3
def remove_char_at(str, n):
    # variable empty to store the new string
    string = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            # store the character in the new variable
            string = string + str[i]
    return string
