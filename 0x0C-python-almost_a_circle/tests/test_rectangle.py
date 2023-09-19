#!/usr/bin/python3
"""Unittest for Base()
"""

import unittest
# from models.base import Base
from models.base import Base
from models import base

class TestBase(unittest.TestCase):
    def Base_id(self):
        result = Base()
        self.assertEqual(result.id, 1)
        result1 = Base()
        self.assertEqual(result1.id, 2)
        result2 = Base()
        self.assertEqual(result2.id, 3)
        result3 = Base(12)
        self.assertEqual(result3.id, 12)
        result4 = Base()
        self.assertEqual(result4.id, 4)
if __name__ == '__main__':
    unittest.main()
