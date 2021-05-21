#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """ A class called rectangle is defined """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    """  The object is initialized with these arguments """

    @property
    def width(self):
        return self.__width
        """ Returns the private attribute of the method """

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
        return self.__height
        """ Returns the private attribute of the method """

    @height.setter
    def height(self, value):
        """ The self.__height attribute is modified """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Method that find the area of a rectangle """

        return self.__width * self.__height
        """ Return the area of a rectangle """

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)
