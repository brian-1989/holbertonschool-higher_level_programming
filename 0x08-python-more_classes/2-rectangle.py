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
        self.__width = width
        self.__height = height

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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method that find the area of a rectangle.
        Return the area of a rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """ Method that find the perimeter of a rectangle.
        Return the perimeter of a rectangle.

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
