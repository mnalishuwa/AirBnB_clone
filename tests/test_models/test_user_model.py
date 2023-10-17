#!/usr/bin/python3


"""
User model unit tests
"""

from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    Unit test class for User class
    """
    def setUp(self):
        """
        Hook, setup test fixtures before execution
        called before implemented test methods
        """
        self.userobject = User()
        print("** setup complete **")

    def test_constructor(self):
        self.assertTrue(isinstance(self.userobject, User))

    def test_inherits_from_base(self):
        self.assertTrue(issubclass(type(self.userobject), BaseModel)
                        and type(self.userobject) != BaseModel)

    def test_attrs(self):
        self.assertTrue(hasattr(self.userobject, 'id'))
        self.assertTrue(hasattr(self.userobject, '__init__'))
        self.assertTrue(hasattr(self.userobject, 'created_at'))
        self.assertTrue(hasattr(self.userobject, 'updated_at'))
        self.assertTrue(hasattr(self.userobject, 'save'))
        self.assertTrue(hasattr(self.userobject, 'to_dict'))
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_attr_type(self):
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.password), str)
        self.assertTrue(isinstance(self.userobject.first_name, str))
        self.assertTrue(isinstance(self.userobject.last_name, str))

    def test_function_docs(self):
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)

    def test_save_method(self):
        self.userobject.save()
        self.assertNotEqual(self.userobject.created_at,
                            self.userobject.updated_at)

    def test_to_dict_method(self):
        object_repr = self.userobject.to_dict()
        self.assertIsInstance(object_repr, dict)

    def tearDown(self):
        """
        Deconstruct class after running tests
        """
        self.userobject = None
        print("** tear down complete**")


if __name__ == '__main__':
    unittest.main()
