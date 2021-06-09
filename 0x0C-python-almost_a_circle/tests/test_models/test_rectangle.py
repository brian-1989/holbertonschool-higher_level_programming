#!/usr/bin/python3
"""
Test to the rectangle class.
"""

from models import rectangle
import unittest
import os

Rectangle = rectangle.Rectangle


class test_rectangle(unittest.TestCase):
    """Cases of requirement.

    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(rectangle.Rectangle.__doc__) > 1)

    def test_of_Pep8_rectangle(self):
        self.assertEqual(os.system("pep8 models/rectangle.py"), 0)

    def test_of_Pep8_test_rectangle(self):
        self.assertEqual(os.system("pep8\
            tests/test_models/test_rectangle.py"), 0)

    def test_to_shebang(self):
        with open('models/rectangle.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')

    """Cases to test the class.

    """
    def test_to_the_values_of_width_and_height(self):
        r1 = Rectangle(40, 45)
        self.assertEqual(r1.width, 40)
        self.assertEqual(r1.height, 45)

    def test_to_the_area_of_rectangle(self):
        r2 = Rectangle(40, 45)
        self.assertEqual(r2.area(), 1800)

    def test_to_update_the_attributes_of_the_class_with_args(self):
        r3 = Rectangle(10, 11, 12, 13, 14)
        r3.update(15, 16, 17, 18, 19)
        self.assertEqual(r3.id, 15)
        self.assertEqual(r3.width, 16)
        self.assertEqual(r3.height, 17)
        self.assertEqual(r3.x, 18)
        self.assertEqual(r3.y, 19)

    def test_to_update_the_attributes_of_the_class_with_kwars(self):
        r4 = Rectangle(id=20, width=21, height=22, x=23, y=24)
        r4.update(id=25, width=26, height=27, x=28, y=29)
        self.assertEqual(r4.__str__(), "[Rectangle] (25) 28/29 - 26/27")

    def test_to_the__str__(self):
        r5 = Rectangle(30, 31, 32, 33, 35)
        self.assertEqual(r5.__str__(), "[Rectangle] (35) 32/33 - 30/31")

    def test_to_the_dictionary(self):
        r6 = Rectangle(36, 37, 38, 39, 40)
        r6_dictionary = r6.to_dictionary()
        _dict = {'id': 40, 'width': 36, 'height': 37, 'x': 38, 'y': 39}
        self.assertEqual(r6_dictionary, _dict)

    """Errors Case to test the class.

    """
    def test_when_the_width_is_a_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('B', 10)

    def test_when_the_width_is_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 10)

    def test_when_the_width_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10)

    def test_when_the_height_is_a_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 'B')

    def test_when_the_height_is_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_when_the_height_is_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

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
