import unittest
max_integer = __import__('6-max_integer')max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer_empty_list(self):
        """test for empty list"""
        self.assertEqual(max_integer([]), None)

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

if __name__ == '__main__':
    unittest.main()
