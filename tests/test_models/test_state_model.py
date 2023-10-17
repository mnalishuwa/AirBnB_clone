#!/usr/bin/python3


"""
State model unit tests
"""

from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """
    Unit test class for State class
    """
    def setUp(self):
        """
        Hook, setup test fixtures before execution
        called before implemented test methods
        """
        self.stateobject = State()
        self.stateobject.name = "Oregon"
        print("** setup complete **")

    def test_constructor(self):
        self.assertTrue(isinstance(self.stateobject, State))

    def test_inherits_from_base(self):
        self.assertTrue(issubclass(type(self.stateobject), BaseModel)
                        and type(self.stateobject) != BaseModel)

    def test_attrs(self):
        self.assertTrue(hasattr(State, 'name'))
        self.assertTrue(hasattr(State, '__init__'))
        self.assertTrue(hasattr(self.stateobject, 'created_at'))
        self.assertTrue(hasattr(self.stateobject, 'updated_at'))
        self.assertTrue(hasattr(self.stateobject, 'save'))
        self.assertTrue(hasattr(self.stateobject, 'to_dict'))

    def test_attr_type(self):
        self.assertTrue(isinstance(self.stateobject.name, str))

    def test_function_docs(self):
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.save.__doc__)
        self.assertIsNotNone(State.to_dict.__doc__)

    def test_save_method(self):
        self.stateobject.save()
        self.assertNotEqual(self.stateobject.created_at,
                            self.stateobject.updated_at)

    def test_to_dict_method(self):
        object_repr = self.stateobject.to_dict()
        self.assertIsInstance(object_repr, dict)

    def tearDown(self):
        """
        Deconstruct class after running tests
        """
        self.stateobject = None
        print("** tear down complete**")


if __name__ == '__main__':
    unittest.main()
