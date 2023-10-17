#!/usr/bin/python3


"""
Base Model Test Suite
"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Unit test class for BaseModel class
    """
    def setUp(self):
        """
        Hook, setup test fixtures before execution
        called before implemented test methods
        """
        self.baseobject = BaseModel()
        print("** setup complete **")

    def test_constructor(self):
        self.assertTrue(isinstance(self.baseobject, BaseModel))

    def test_attrs(self):
        self.assertTrue(hasattr(self.baseobject, 'id'))
        self.assertTrue(hasattr(self.baseobject, 'created_at'))
        self.assertTrue(hasattr(self.baseobject, 'updated_at'))
        self.assertTrue(hasattr(self.baseobject, 'save'))
        self.assertTrue(hasattr(self.baseobject, 'to_dict'))

    def test_function_docs(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_save_method(self):
        self.baseobject.save()
        self.assertNotEqual(self.baseobject.created_at,
                            self.baseobject.updated_at)

    def test_to_dict_method(self):
        object_repr = self.baseobject.to_dict()
        self.assertIsInstance(object_repr, dict)

    def tearDown(self):
        """
        Deconstruct class after running tests
        """
        self.baseobject = None
        print("** tear down complete**")


if __name__ == '__main__':
    unittest.main()
