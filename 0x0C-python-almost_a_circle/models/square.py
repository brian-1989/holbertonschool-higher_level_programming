#!/usr/bin/python3
"""
Square.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits the class Rectangle.

    """
    def __init__(self, size, x=0, y=0, id=None):
        """inital method the store the arguments
        of the class square.

        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """method that convert objects into strings.
        Return the object in string.

        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """function getter of size.
        Return the private attribute of size.

        """
        return self.width

    @size.setter
    def size(self, size):
        """function setter of size is modified.

        """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size is 0 or size < 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size
