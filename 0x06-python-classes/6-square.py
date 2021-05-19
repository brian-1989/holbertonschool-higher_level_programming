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
        if type(value[0]) and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ method to calculate the area of a square """
    def area(self):
        _area = self.__size**2

        """ Returns: the area of a square. """
        return _area

    """ method that prints in stdout the square with the character and space"""
    def my_print(self):
        if self.__size is 0:
            print(end="\n")
        for i in range(0, self.__size):
            if self.__position[0] is not 0 or self.__position[1] is not 0:
                for j in range(0, self.__position[0]):
                    print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print(end="\n")
        if self.__position[1] > 0:
            for i in range(0, self.__position[1]):
                print(end="\n")
