#!/usr/bin/python3
"""
Base.
"""


import json


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

    def to_json_string(list_dictionaries):
        """method that converts a dictionary in a string.
        Return the JSON string representation of list_dictionaries.

        """
        if list_dictionaries is None or list_dictionaries is []:
            return []
        return json.dumps(list_dictionaries)
