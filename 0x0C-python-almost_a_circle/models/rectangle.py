#!/usr/bin/python3
"""
Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits the class Base.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initial method that store the arguments.
        of the class Rectangle.
        Args:
            width: width of rectangle.
            height: height of rectangle.
            x: dimensions of rectangle.
            y: dimensions of rectangle.
            id: integer.

        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width is 0 or width < 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height is 0 or height < 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width is 0 or width < 0:
            raise ValueError("width must be > 0")
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
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height is 0 or height < 0:
            raise ValueError("height must be > 0")
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
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """method that find the area of a rectangle.
        Return the area of a rectangle.

        """
        return self.width * self.height

    def display(self):
        """method that print in screen a rectangle.
        with the character "#".

        """
        for _jumpline in range(self.y):
            print(end="\n")
        for _height in range(self.height):
            for _space in range(self.x):
                print(" ", end="")
            for _width in range(self.width):
                print("#", end="")
            print(end="\n")

    def __str__(self) -> str:
        """method that convert Python objects into strings.
        Return the object in string.

        """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """method that update the arguments of each attribute
        with the argument kwargs.

        """
        for key, value in kwargs.items():
            setattr(self, key, value)
