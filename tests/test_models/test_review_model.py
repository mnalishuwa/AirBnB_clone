#!/usr/bin/python3


"""
Review model unit tests
"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """
    Unit test class for Review class
    """
    def setUp(self):
        """
        Hook, setup test fixtures before execution
        called before implemented test methods
        """
        self.reviewobject = Review()
        self.reviewobject.place_id = "0619 Palatine Hill"
        self.reviewobject.user_id = "Mukwa"
        self.text = "Awesome"
        print("** setup complete **")

    def test_constructor(self):
        self.assertTrue(isinstance(self.reviewobject, Review))

    def test_inherits_from_base(self):
        self.assertTrue(issubclass(type(self.reviewobject), BaseModel)
                        and type(self.reviewobject) != BaseModel)

    def test_attrs(self):
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))
        self.assertTrue(hasattr(Review, '__init__'))
        self.assertTrue(hasattr(self.reviewobject, 'created_at'))
        self.assertTrue(hasattr(self.reviewobject, 'updated_at'))
        self.assertTrue(hasattr(self.reviewobject, 'save'))
        self.assertTrue(hasattr(self.reviewobject, 'to_dict'))
        self.assertTrue(hasattr(self.reviewobject, 'id'))

    def test_attr_type(self):
        self.assertTrue(isinstance(self.reviewobject.place_id, str))
        self.assertTrue(isinstance(self.reviewobject.user_id, str))
        self.assertTrue(isinstance(self.reviewobject.text, str))

    def test_function_docs(self):
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.save.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)

    def test_save_method(self):
        self.reviewobject.save()
        self.assertNotEqual(self.reviewobject.created_at,
                            self.reviewobject.updated_at)

    def test_to_dict_method(self):
        object_repr = self.reviewobject.to_dict()
        self.assertIsInstance(object_repr, dict)

    def tearDown(self):
        """
        Deconstruct class after running tests
        """
        self.reviewobject = None
        print("** tear down complete**")


if __name__ == '__main__':
    unittest.main()
