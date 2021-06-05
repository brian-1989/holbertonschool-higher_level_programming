#!/usr/bin/python3
"""
Base.
"""


import json
from os import path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that serialize a data struct in a string.
        Return the JSON string representation of list_dictionaries.

        """
        if list_dictionaries is None or list_dictionaries is []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method that write a un file the JSON string representation
        of list_objs.

        """
        my_list = []
        for i in list_objs:
            my_list.append(i.__dict__)
        if path.exists("{}.json".format(cls.__name__)):
            with open("{}.json".format(cls.__name__), 'a') as text:
                string_list = Base.to_json_string(my_list)
                if list_objs is None:
                    text.write("[]")
                else:
                    text.write(string_list)
                text.close()
        else:
            with open("{}.json".format(cls.__name__), 'w') as text:
                string_list = Base.to_json_string(my_list)
                if list_objs is None:
                    text.write("[]")
                else:
                    text.write(string_list)
                text.close()

    def from_json_string(json_string):
        """method that deserialize a string to data struct.
        Return the list of the JSON string representation json_string.

        """
        if json_string is None or json_string is ():
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """methon that created a instance and update
        the attributtes.
        Return the attributes update.

        """
        dummy = cls(4, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """method that that returns a list of instances.

        """
        my_list = []
        if path.exists("{}.json".format(cls.__name__)):
            with open("{}.json".format(cls.__name__), 'r') as text:
                my_list_dict = cls.from_json_string(text.read())
                for i_dict in my_list_dict:
                    my_list.append(cls.create(**i_dict))
            return my_list
        else:
            return []
