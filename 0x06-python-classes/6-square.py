#!/usr/bin/python3
""" define class square"""


class Square:
    """ method Private instance attribute """

    def __init__(self, size=0, position=(0, 0)):
        """ Args:
            size: size of square.
            position: tuple with de space and jump line """
        self.__size = size
        self.__position = position
        for i in position:
            if type(i) is not int:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if len(position) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if i < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """ Returns: the value of self.__size. """
        return self.__size

    """ method to modify the attribute size"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Returns: the value of self.__position. """
        return self.__position

    """ method to modify the attribute position"""
    @position.setter
    def position(self, value):
        for i in value:
            if type(i) is not int:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if len(value) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if i < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")

    def area(self):
        """ method to calculate the area of a square """
        _area = self.__size**2

        """ Returns: the area of a square. """
        return _area

    def my_print(self):
        """ method that prints in stdout the square with the "#" and " " """
        if self.__size is 0:
            print(end="\n")
        if self.__size != 0:
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print(end="\n")
            if self.__position[1] > 0:
                for i in range(0, self.__position[1]):
                    print(end="\n")
