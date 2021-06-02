#!/usr/bin/python3
"""
Overwrite file.
"""


def append_write(filename="", text=""):
    """function that overwrite a text in a file.
    Args:
        filename: name of file.
        text: text a write in the file.
    Return the character number.

    """
    with open(filename, 'a') as _text:
        write_text = _text.write(text)
        _text.close()
        return write_text
