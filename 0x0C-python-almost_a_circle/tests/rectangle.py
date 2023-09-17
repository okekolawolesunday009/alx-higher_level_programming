"""Unittest for Base()
"""

import unittest
from models.base import Base

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
