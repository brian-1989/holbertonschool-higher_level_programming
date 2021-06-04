#!/usr/bin/python3
"""
Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits the class Base.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initial method that store the arguments,
        of the class Rectangle.
        Args:
            width: width of rectangle
            height: height of rectangle
            x: dimensions of rectangle
            y: dimensions of rectangle
            id: integer

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """function getter of width.
        Return the private attribute of width.

        """
        return self.__width

    @width.setter
    def width(self, width):
        """function setter of width is modified.

        """
        self.__width = width

    @property
    def height(self):
        """function getter of height.
        Return the private attribute of height.

        """
        return self.__height

    @height.setter
    def height(self, height):
        """function height of width is modified.

        """
        self.__height = height

    @property
    def x(self):
        """function getter of x.
        Return the private attribute of x.

        """
        return self.__x

    @x.setter
    def x(self, x):
        """function x of width is modified.

        """
        self.__x = x

    @property
    def y(self):
        """function getter of y.
        Return the private attribute of y.

        """
        return self.__y

    @y.setter
    def y(self, y):
        """function y of width is modified.

        """
        self.__y = y
