"""Unittest for max_integer([..])
"""

import unittest
from models.base import Base

max_integer = __import__('6-max_integer').max_integer

class TestBase(unittest.TestCase):
    def Base_id(self):
        result = Base()
        self.assertEqual(result, 1)
        result = Base()
        self.assertEqual(result, 2)
        result = Base()
        self.assertEqual(result, 3)
        result = Base(12)
        self.assertEqual(result, 12)
        result = Base()
        self.assertEqual(result, 4)

    def SubClass_Rectangle(self):
        result = Rectangle(10, 2)
        self.assertEqual(result, 2)
        