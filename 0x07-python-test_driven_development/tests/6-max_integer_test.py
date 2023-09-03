#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def max_integer(self):
        result = max_integer([1, 2, 3, 4], 4)
        self.assertEqual(result, 4)
