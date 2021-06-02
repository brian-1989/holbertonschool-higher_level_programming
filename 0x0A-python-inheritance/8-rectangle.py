#!/usr/bin/python3
"""
base geometry
"""

BaseGeometry = __import__('7-base_geometry').BaseException


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
