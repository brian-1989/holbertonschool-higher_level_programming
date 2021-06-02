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
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)
        self.__str__()

    def area(sefl):
        """method that that get the area of a square.
        Return the area of a square.

        """
        return sefl.__size**2
