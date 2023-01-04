#!/usr/bin/python3
# 6-max_integer_test.py
"""Unit tsts for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
     """Define unittests for max_integer([..])."""

     def test_ordered_list(self):
         """Test an ordered list of integers."""
         ordered = [1, 2, 3, 4]
         self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Tests a list with a beginning max value"""
        max_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_list), 4)

    def test_one_element_list(self):
        """Tests with just one element"""
        el = [7]
        self.assertEqual(max_integer(el), 7)

    def test_empty_list(self):
        """Test when list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_string(self):
        """Tests function with a string"""
        strr = "phil"
        self.assertEqual(max_integer(strr), 'p')

    def test_floats(self):
        """Tests decimal numbers"""
        floats = [1.34, -0.45, 112.88, 45.0]
        self.assertEqual(max_integer(floats), 'p')

    def test_ints_and_floats(self):
         """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_empty_string(self):
        """Test an empty string."""
         self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        def test_list_of_strings(self)
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

if __name__ == '__main__':
    unittest.main()
