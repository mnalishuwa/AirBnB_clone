#!/usr/bin/python3


"""
Review model unit tests
"""

from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """
    Unit test class for Place class
    """
    def setUp(self):
        """
        Hook, setup test fixtures before execution
        called before implemented test methods
        """
        self.placeobject = Place()
        self.placeobject.city_id = "Portland"
        self.placeobject.user_id = "Nash"
        print("** setup complete **")

    def test_constructor(self):
        self.assertTrue(isinstance(self.placeobject, Place))

    def test_inherits_from_base(self):
        self.assertTrue(issubclass(type(self.placeobject), BaseModel)
                        and type(self.placeobject) != BaseModel)

    def test_attrs(self):
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))
        self.assertTrue(hasattr(self.placeobject, 'created_at'))
        self.assertTrue(hasattr(self.placeobject, 'updated_at'))
        self.assertTrue(hasattr(self.placeobject, 'save'))
        self.assertTrue(hasattr(self.placeobject, 'to_dict'))
        self.assertTrue(hasattr(self.placeobject, 'id'))

    def test_attr_type(self):
        self.assertTrue(isinstance(self.placeobject.city_id, str))
        self.assertTrue(isinstance(self.placeobject.user_id, str))
        self.assertTrue(isinstance(self.placeobject.number_rooms, int))
        self.assertTrue(isinstance(self.placeobject.latitude, float))
        self.assertTrue(isinstance(self.placeobject.amenity_ids, list))

    def test_function_docs(self):
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.save.__doc__)
        self.assertIsNotNone(Place.to_dict.__doc__)

    def test_save_method(self):
        self.placeobject.save()
        self.assertNotEqual(self.placeobject.created_at,
                            self.placeobject.updated_at)

    def test_to_dict_method(self):
        object_repr = self.placeobject.to_dict()
        self.assertIsInstance(object_repr, dict)

    def tearDown(self):
        """
        Deconstruct class after running tests
        """
        self.placeobject = None
        print("** tear down complete**")


if __name__ == '__main__':
    unittest.main()
