#!/usr/bin/python3
"""
Text
"""


def text_indentation(text):
    """Function that print a text and in each character
    specified makes a jump line.
    
    """
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    jump = False
    while(i < len(text)):
        if text[i] is " " and jump is False or text[i] is "\n" and jump is False:
            i += 1
            continue
        elif text[i] == " " and text[i + 1] == " " and text[i + 1]:
            jump = False
            i += 1
        elif text[i] == "." or text[i] == "?" or text[i] == ":":
            jump = False
            print("{}".format(text[i]), end="")
            print(end="\n\n")
            i += 1
        else:
            jump = True
            print("{}".format(text[i]), end="")
            i += 1
