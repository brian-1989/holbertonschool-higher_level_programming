#!/usr/bin/python3
""" A class called rectangle is defined """


class Rectangle:
    """  The object is initialized with these arguments """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Returns the private attribute of the method """
        return self.__width

    @width.setter
    def width(self, value):
        """ The self.__value attribute is modified """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns the private attribute of the method """
        return self.__height

    @height.setter
    def height(self, value):
        """ The self.__height attribute is modified """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
