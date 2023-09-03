#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_trueValue(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_values(self):
         result = max_integer([], )
         self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
