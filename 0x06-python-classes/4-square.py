#!/usr/bin/python3
""" define class square"""


class Square:
    """ Private instance attribute """

    def __init__(self, size=0):
        """ Args:
        size: The first parameter. """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """ Function to calculate the area of a square """

    def area(self):
        _area = self.__size**2
        """ Returns:
        the area of a square. """
        return _area
    """ Function to calculate the area of a square """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
