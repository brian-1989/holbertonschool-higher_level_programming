#!/usr/bin/python3
"""
Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits.

    """
    def __init__(self, size):
        """initial method that take the size of square.
        Agrs:
            size: size of square.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """method that return the description of a square.

        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(sefl):
        """method that that get the area of a square.
        Return the area of a square.

        """
        return sefl.__size**2
