import unittest
from models.city import City
import datetime
from uuid import UUID

class TestCity(unittest.TestCase):

    def setUp(self):
        """
        Set up a fresh instance of City for each test.
        """
        self.test_city = City()

    def test_subclass(self):
        """
        Test if City is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_has_attributes(self):
        """
        Test if the City instance has the expected attributes.
        """
        self.assertTrue(hasattr(self.test_city, 'name'))
        self.assertTrue(hasattr(self.test_city, 'state_id'))

    def test_id_is_valid_uuid(self):
        """
        Test if the 'id' attribute is a valid UUID.
        """
        self.assertTrue(UUID(self.test_city.id))

    def test_created_at_is_datetime(self):
        """
        Test if the 'created_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_city.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if the 'updated_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_city.updated_at, datetime.datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the 'to_dict' method returns a dictionary with expected keys.
        """
        model_dict = self.test_city.to_dict()
        self.assertIn('name', model_dict)
        self.assertIn('state_id', model_dict)

    def test_str_representation(self):
        """
        Test if the string representation of City contains expected information.
        """
        str_repr = str(self.test_city)
        self.assertIn("[City]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn(str(self.test_city.id), str_repr)

if __name__ == '__main__':
    unittest.main()
