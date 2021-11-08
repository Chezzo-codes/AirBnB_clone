#!/usr/bin/python3
"""
Unittests for BaseModel class
"""
from models.base_model import BaseModel
import unittest
import pep8


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.baseClass = BaseModel()

    @classmethod
    def tearDownClass(cls):
        del cls.baseClass

    def test_pep8_style(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        test = style.check_files(['models/base_model.py'])
        self.assertEqual(test.total_errors, 0, "fix pep8")


if __name__ == '__main__':
    unittest.main()
