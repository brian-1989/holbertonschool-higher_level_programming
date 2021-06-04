#!/usr/bin/python3
"""
Base.
"""


class Base:
    """class base to the proyect.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initial method that store the arguments.
        Args:
            id: integer.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
