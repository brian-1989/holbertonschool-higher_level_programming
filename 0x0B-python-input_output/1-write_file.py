#!/usr/bin/python3
"""
Write in a file.
"""


def write_file(filename="", text=""):
    """function that writes a text in a file and if the file
    does not exist, it creates it.
    Args:
        filename: name of file
        text: text a write in the file
    Return the character number.

    """
    with open(filename, 'w') as _text:
        write_text = _text.write(text)
        _text.close()
        return write_text
