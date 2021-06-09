#!/usr/bin/python3
"""
Test to the base class.
"""


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

    def test_to_shebang(self):
        with open('models/base.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')

    """Cases to test the class.

    """
    def test_when_the_id_is_None(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 2)

    def test_when_the_id_is_positive(self):
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_when_the_id_is_negative(self):
        b1 = Base(-100)
        self.assertEqual(b1.id, -100)

    def test_when_the_id_is_float(self):
        b1 = Base(10.9)
        self.assertEqual(b1.id, 10.9)

    def test_to_validate_the_JSON_string_representation_of_list_dictionaries(
            self):
        r1 = Rectangle(45, 67)
        _dict = r1.to_dictionary()
        _json_dict_str = Base.to_json_string([_dict])
        _type = isinstance(_json_dict_str, str)
        self.assertEqual(_type, True)
        _json_dict = Base.from_json_string(_json_dict_str)
        test_dict = [{"id": 1, "width": 45, "height": 67, "x": 0, "y": 0}]
        self.assertEqual(_json_dict, test_dict)

    def test_to_validate_the_JSON_string_of_list_dictionaries_empty(self):
        _json_dict_str = Base.to_json_string([])
        _type = isinstance(_json_dict_str, str)
        self.assertEqual(_type, True)
        _json_dict = Base.from_json_string(_json_dict_str)
        test_dict = []
        self.assertEqual(_json_dict, test_dict)

    def test_to_validate_the_dict_of_the_JSON_string_representation(self):
        test_dict = '[{"id": 2, "width": 46, "height": 68, "x": 0, "y": 0}]'
        _json_dict_str = Base.to_json_string(test_dict)
        _type = isinstance(_json_dict_str, str)
        self.assertEqual(_type, True)

    def test_to_validate_the_dict_of_the_JSON_string_is_None(self):
        _json_dict_str = Base.to_json_string(None)
        self.assertEqual(_json_dict_str, "[]")

if __name__ == "__main__":
    unittest.main()
