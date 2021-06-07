#!/usr/bin/python3

from models import base, rectangle
import unittest
import os

Base = base.Base
Rectangle = rectangle.Rectangle


class test_base(unittest.TestCase):
    """Cases of requirement.

    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(Base.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(base.Base.__doc__) > 1)

    def test_of_Pep8_base(self):
        self.assertEqual(os.system("pep8 models/base.py"), 0)

    def test_of_Pep8_test_base(self):
        self.assertEqual(os.system("pep8 tests/test_models/test_base.py"), 0)

    """Cases of requirement.

    """
    def test_when_the_id_is_None(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 3)

    def test_when_the_id_is_integer(self):
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_to_validate_the_JSON_string_representation_of_list_dictionaries(
            self):
        r1 = Rectangle(45, 67)
        _dict = r1.to_dictionary()
        _json_dict = Base.to_json_string(_dict)
        _type = isinstance(_json_dict, str)
        self.assertEqual(_type, True)

    def test_to_validate_the_dict_of_the_JSON_string_representation(self):
        r1 = Rectangle(45, 67)
        _dict = r1.to_dictionary()
        _json_dict = Base.to_json_string(_dict)
        _json_dict_list = Base.from_json_string(_json_dict)
        _type = isinstance(_json_dict_list, dict)
        self.assertEqual(_type, True)
