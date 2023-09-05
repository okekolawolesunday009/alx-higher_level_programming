#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_postiveValues(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

        result = max_integer([1, 4, 3, 3])
        self.assertEqual(result, 4)

        result = max_integer([4, 4, 3, 3])
        self.assertEqual(result, 4)

        result = max_integer([4, 4, 4, 4])
        self.assertEqual(result, 4)

        result = max_integer([1.1, 2.3, 3.0, 4.0])
        self.assertEqual(result, 4.0)

        result = max_integer([4.11, 4.12, 4.64, 4.7])
        self.assertEqual(result, 4.7)

        result = max_integer([1, 2, 3, 4, 5, 6, 7, 8, 0])
        self.assertEqual(result, 8)

        result = max_integer(["derek", "shade"])
        self.assertEqual(result, 's')

        result = max_integer([20])
        self.assertEqual(result, 20)

        result = max_integer((1, 2, 3))
        self.assertEqual(result, 3)

        result = max_integer([[1, 2, 3], [2, 3, 6]], )
        self.assertEqual(result, 6)

    def test_negativeValues(self):
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -4)

        result = max_integer([-1, -4, 3, -3])
        self.assertEqual(result, 3)

        result = max_integer([-4, -4, -3, -3])
        self.assertEqual(result, -4)

        result = max_integer([-1.1, -2.3, -3.0, -4.0])
        self.assertEqual(result, -4.0)

        result = max_integer([-1, -2, -3, -4, -5, -6, -7, -8, 0])
        self.assertEqual(result, -8)
    
    def test_compositeValues(self):
        result = max_integer([])
        self.assertEqual(result, None)

        result = max_integer(["Dereke"])
        self.assertEqual(result, 3)

        result = max_integer("shade")
        self.assertEqual(result, 's')

        result = max_integer("Dd")
        self.assertEqual(result, 'd')

        result = max_integer(None)
        self.assertRaises(TypeError)

        result = max_integer({1, 2, 3})
        self.assertRaises(TypeError)

        result = max_integer(5)
        self.assertRaises(TypeError)

        result = max_integer([0, 0, 0])
        self.assertRaises(result, 0)

        result = max_integer({})
        self.assertRaises(result, None)

        result = max_integer(())
        self.assertRaises(result, None)

if __name__ == '__main__':
    unittest.main()
