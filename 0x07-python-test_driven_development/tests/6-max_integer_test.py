#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_to_normal_use(self):
        self.assertAlmostEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_when_max_beginning(self):
        self.assertAlmostEqual(max_integer([10, 1, 2, 9]), 10)

    def test_when_max_end(self):
        self.assertAlmostEqual(max_integer([5, 6, 7, 20]), 20)

    def test_when_max_half(self):
        self.assertAlmostEqual(max_integer([5, 30, 7, 20]), 30)

    def test_when_is_Empty(self):
        self.assertIsNone(max_integer([]))

    def test_when_is_negative(self):
        self.assertAlmostEqual(max_integer([-9, -12, -4, -30, -1]), -1)

    def test_when_is_only_number(self):
        self.assertAlmostEqual(max_integer([10]), 10)
