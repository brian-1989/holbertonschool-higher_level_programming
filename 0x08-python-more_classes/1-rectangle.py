#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """ A class called rectangle is defined """

    def __init__(self, width=0, height=0):
        """  The object is initialized with these arguments.
        Args:
        width: width of rectangle.
        height: heigth of rectangle.

        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the private attribute of the method.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """ The self.__value attribute is modified.

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the private attribute of the method.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """The self.__height attribute is modified.

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
