"""Unittest for Base()
"""

import unittest
from models.base import Base
from models import base
Base = Base
to_json_string = Base.to_json_string
save_to_file = Base.save_to_file
from_json_string = Base.from_json_string
create = Base.create
load_from_file = Base.load_from_file


class TestBaseClass(unittest.TestCase):

    """Class for unittest of Base class"""

    def test_documentation(self):
        """Test documentation"""

        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """Test documentation"""

        self.assertTrue(len(Base.__doc__) > 0)

    def test_json_string_doc(self):
        """Test documentation"""

        self.assertTrue(len(to_json_string.__doc__) > 0)

    def test_save_file(self):
        """Test documentation"""

        self.assertTrue(len(save_to_file.__doc__) > 0)

    def test_from_json(self):
        """Test documentation"""

        self.assertTrue(len(from_json_string.__doc__) > 0)

    def test_create(self):
        """Test documentation"""

        self.assertTrue(len(create.__doc__) > 0)

    def test_load_file(self):
        """Test documentation"""

        self.assertTrue(len(load_from_file.__doc__) > 0)

class TestBase(unittest.TestCase):
    """test for id"""
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
if __name__ == '__main__':
    unittest.main()
