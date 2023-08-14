#!/usr/bin/python3

import unittest
from models.state import State
import datetime
from uuid import UUID

class TestState(unittest.TestCase):
        """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'State'
        self.value = State

    def setUp(self):
        """
        Set up a fresh instance of State for each test.
        """
        self.test_state = State()

    def test_subclass(self):
        """
        Test if State is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_has_attributes(self):
        """
        Test if the State instance has the expected attributes.
        """
        self.assertTrue(hasattr(self.test_state, 'name'))

    def test_id_is_valid_uuid(self):
        """
        Test if the 'id' attribute is a valid UUID.
        """
        self.assertTrue(UUID(self.test_state.id))

    def test_created_at_is_datetime(self):
        """
        Test if the 'created_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_state.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if the 'updated_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_state.updated_at, datetime.datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the 'to_dict' method returns a dictionary with expected keys.
        """
        model_dict = self.test_state.to_dict()
        self.assertIn('name', model_dict)

    def test_str_representation(self):
        """
        Test if the string representation of State contains expected information.
        """
        str_repr = str(self.test_state)
        self.assertIn("[State]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn(str(self.test_state.id), str_repr)

if __name__ == '__main__':
    unittest.main()
