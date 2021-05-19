#!/usr/bin/python3
""" define class square"""


class Square:
    """ method Private instance attribute """

    def __init__(self, size=0):
        """ size: The first parameter. """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ method to calculate the area of a square """
    def area(self):
        _area = self.__size**2

        """ Returns:the area of a square. """
        return _area

    """ method to calculate the area of a square """
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

    """ method that prints in stdout the square with the character """
    def my_print(self):
        if self.__size is 0:
            print(end="\n")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print(end="\n")
