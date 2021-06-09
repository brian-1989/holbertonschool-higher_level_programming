#!/usr/bin/python3
"""
Test to the square class.
"""

from models import rectangle, square
import unittest
import os

Rectangle = rectangle.Rectangle
Square = square.Square


class test_rectangle(unittest.TestCase):
    """Cases of requirement.

    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(Square.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(square.Square.__doc__) > 1)

    def test_of_Pep8_square(self):
        self.assertEqual(os.system("pep8 models/square.py"), 0)

    def test_of_Pep8_square(self):
        self.assertEqual(os.system("pep8 tests/test_models/test_square.py"), 0)

    """Cases to test the class.

    """
    def test_to_the_values_of_size(self):
        s1 = Square(10)
        self.assertEqual(s1.width, 10)

    def test_to_the_area_of_square(self):
        s2 = Square(11)
        self.assertEqual(s2.area(), 121)

    def test_to_update_the_attributes_of_the_class_with_args(self):
        s3 = Square(12, 13, 14, 15)
        s3.update(16, 17, 18, 19)
        self.assertEqual(s3.__str__(), "[Square] (16) 18/19 - 17")

    def test_to_update_the_attributes_of_the_class_with_kwars(self):
        s4 = Square(20, 21, 22, 23)
        s4.update(24, 25, 26, 27)
        self.assertEqual(s4.__str__(), "[Square] (24) 26/27 - 25")

    def test_to_the__str__(self):
        s5 = Square(28, 29, 30, 31)
        self.assertEqual(s5.__str__(), "[Square] (31) 29/30 - 28")

    def test_to_the_dictionary(self):
        r6 = Rectangle(32, 33, 34, 35, 36)
        r6_dictionary = r6.to_dictionary()
        _dict = {'id': 36, 'width': 32, 'height': 33, 'x': 34, 'y': 35}
        self.assertEqual(r6_dictionary, _dict)
        self.assertEqual(type(r6_dictionary), dict)

    def test_to_the_type_dictionary(self):
        r6 = Rectangle(37, 38, 39, 40, 41)
        r6_dictionary = r6.to_dictionary()
        _dict = {'id': 41, 'width': 37, 'height': 38, 'x': 39, 'y': 40}
        self.assertEqual(type(r6_dictionary), dict)

    """Errors Case to test the class.

    """
    def test_when_the_size_is_a_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('B')

    def test_when_the_size_is_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)

    def test_when_the_size_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_when_the_x_is_a_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 11, 'B')

    def test_when_the_x_is_zero(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 11, -2)

    def test_when_the_y_is_a_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 11, 12, 'B')

    def test_when_the_y_is_zero(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 11, 12, -2)

if __name__ == "__main__":
    unittest.main()
