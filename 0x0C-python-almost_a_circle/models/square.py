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

    def update(self, *args, **kwargs):
        """method that update the arguments of each attribute
        with the arguments args and kwargs.

        """
        if args:
            my_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, my_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method that adding in a dictionary the attributes of
        the class square.
        Return the dictionary with the attributes.

        """
        my_dic = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
            }
        return my_dic
