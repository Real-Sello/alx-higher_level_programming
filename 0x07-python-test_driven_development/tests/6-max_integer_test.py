#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer')max_integer


class TestMaxInteger(unittest.TestCase):
        """Unit test for max_integer function
        """

    def test_max_integer_empty_list(self):
        """test for empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_list_of_ints(self):
        """test for positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_integer_list_of_mixed_types(self):
        """test for possible errors"""
        self.assertEqual(max_integer([1, 2, 'a', 4]), 4)
        self.assertEqual(max_integer(['a', 2, 'b', 4]), 4)

    def test_max_integer_list_of_negatives(self):
        """test for negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

     def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

if __name__ == '__main__':
    unittest.main()
