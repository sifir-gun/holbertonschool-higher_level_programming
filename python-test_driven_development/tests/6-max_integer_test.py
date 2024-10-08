#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 3, -2, 7, 4]), 7)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.6]), 3.6)

    def test_list_with_same_values(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_string(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
