#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """ A class called rectangle is defined.

    """
    number_of_instances = 0

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
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Method that find the area of a rectangle.
        Return the area of a rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Method that find the perimeter of a rectangle.
        Return the perimeter of a rectangle.

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self) -> str:
        """Method that return a rectangle.
        Return a string with the rectangle.

        """
        _rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return _rectangle
        for _width in range(0, self.__height):
            for _height in range(0, self.__width):
                _rectangle += "#"
            if _width < self.__height - 1:
                _rectangle += "\n"
        return _rectangle

    def __repr__(self) -> str:
        """Method that makes a representation of a rectangle.
        Return the width and heigth of a rectangle to create a new instace.

        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self)->str:
        """ Method to delete a instace and print the message.

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
