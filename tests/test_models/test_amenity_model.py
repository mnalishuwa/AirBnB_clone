#!/usr/bin/python3


"""
State model unit tests
"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """
    Unit test class for Amenity class
    """
    def setUp(self):
        """
        Hook, setup test fixtures before execution
        called before implemented test methods
        """
        self.amenityobject = Amenity()
        self.amenityobject.name = "Swimming Pool"
        print("** setup complete **")

    def test_constructor(self):
        self.assertTrue(isinstance(self.amenityobject, Amenity))

    def test_inherits_from_base(self):
        self.assertTrue(issubclass(type(self.amenityobject), BaseModel)
                        and type(self.amenityobject) != BaseModel)

    def test_attrs(self):
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertTrue(hasattr(Amenity, '__init__'))
        self.assertTrue(hasattr(self.amenityobject, 'created_at'))
        self.assertTrue(hasattr(self.amenityobject, 'updated_at'))
        self.assertTrue(hasattr(self.amenityobject, 'save'))
        self.assertTrue(hasattr(self.amenityobject, 'to_dict'))

    def test_attr_type(self):
        self.assertTrue(isinstance(self.amenityobject.name, str))

    def test_function_docs(self):
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)

    def test_save_method(self):
        self.amenityobject.save()
        self.assertNotEqual(self.amenityobject.created_at,
                            self.amenityobject.updated_at)

    def test_to_dict_method(self):
        object_repr = self.amenityobject.to_dict()
        self.assertIsInstance(object_repr, dict)

    def tearDown(self):
        """
        Deconstruct class after running tests
        """
        self.amenityobject = None
        print("** tear down complete**")


if __name__ == '__main__':
    unittest.main()
