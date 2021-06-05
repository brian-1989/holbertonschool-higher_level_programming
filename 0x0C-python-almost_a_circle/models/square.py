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
