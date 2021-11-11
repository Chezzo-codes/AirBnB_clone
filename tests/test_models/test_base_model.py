#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os
import pep8
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.baseClass = BaseModel()

    @classmethod
    def tearDownClass(cls):
        del cls.baseClass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_check_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        self.assertTrue(isinstance(self.baseClass, BaseModel))

    def test_save(self):
        self.baseClass.save()
        self.assertNotEqual(self.baseClass.created_at, self.baseClass.updated_at)

    def test_to_dict(self):
        base12_dict = self.base12.to_dict()
        self.assertEqual(self.base12.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base12_dict['created_at'], str)
        self.assertIsInstance(base12_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
