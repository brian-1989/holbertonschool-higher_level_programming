#!/usr/bin/python3
"""
Read file.
"""


def read_file(filename=""):
    """function that read the text of a file.

    """
    with open(filename, 'r', encoding="utf-8") as text:
        read_text = text.read()
        print("{}".format(read_text))
        text.close()
