#!/usr/bin/python3
"""
base geometry
"""


class BaseGeometry:
    """class base geometry.

    """
    def area(self):
        """method that raise an exception.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates the argumnets value and created
        an exception.
        Args:
            name: name of user
            value: value to validates

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value is 0 or value < 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class receiving the inheritance BaseGeometry.

    """
    def __init__(self, width, height):
        """initial method that receiving the arguments.
        Agrgs:
            width: width of Rectangle.
            height: height of Rectangle.

        """
        self.__width = width
        self.__height = height
        if type(width) is not int:
            self.integer_validator("width", width)
        if type(height) is not int:
            self.integer_validator("height", height)
