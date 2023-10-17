#!/usr/bin/python3


"""
City model unit tests
"""

from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
    Unit test class for City class
    """
    def setUp(self):
        """
        Hook, setup test fixtures before execution
        called before implemented test methods
        """
        self.cityobject = City()
        self.cityobject.name = "Portland"
        self.cityobject.state_id = "OR"
        print("** setup complete **")

    def test_constructor(self):
        self.assertTrue(isinstance(self.cityobject, City))

    def test_inherits_from_base(self):
        self.assertTrue(issubclass(type(self.cityobject), BaseModel)
                        and type(self.cityobject) != BaseModel)

    def test_attrs(self):
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertTrue(hasattr(City, '__init__'))
        self.assertTrue(hasattr(self.cityobject, 'created_at'))
        self.assertTrue(hasattr(self.cityobject, 'updated_at'))
        self.assertTrue(hasattr(self.cityobject, 'save'))
        self.assertTrue(hasattr(self.cityobject, 'to_dict'))
        self.assertTrue(hasattr(self.cityobject, 'id'))

    def test_attr_type(self):
        self.assertTrue(isinstance(self.cityobject.name, str))
        self.assertTrue(isinstance(self.cityobject.state_id, str))

    def test_function_docs(self):
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.save.__doc__)
        self.assertIsNotNone(City.to_dict.__doc__)

    def test_save_method(self):
        self.cityobject.save()
        self.assertNotEqual(self.cityobject.created_at,
                            self.cityobject.updated_at)

    def test_to_dict_method(self):
        object_repr = self.cityobject.to_dict()
        self.assertIsInstance(object_repr, dict)
        self.assertTrue('id' in self.cityobject.__dict__)

    def tearDown(self):
        """
        Deconstruct class after running tests
        """
        self.cityobject = None
        print("** tear down complete**")


if __name__ == '__main__':
    unittest.main()
