import unittest
from models.user import User
import datetime
from uuid import UUID

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up a fresh instance of User for each test.
        """
        self.test_user = User()

    def test_subclass(self):
        """
        Test if User is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_has_attributes(self):
        """
        Test if the User instance has the expected attributes.
        """
        self.assertTrue(hasattr(self.test_user, 'email'))
        self.assertTrue(hasattr(self.test_user, 'password'))
        self.assertTrue(hasattr(self.test_user, 'first_name'))
        self.assertTrue(hasattr(self.test_user, 'last_name'))

    def test_id_is_valid_uuid(self):
        """
        Test if the 'id' attribute is a valid UUID.
        """
        self.assertTrue(UUID(self.test_user.id))

    def test_created_at_is_datetime(self):
        """
        Test if the 'created_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_user.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if the 'updated_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_user.updated_at, datetime.datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the 'to_dict' method returns a dictionary with expected keys.
        """
        model_dict = self.test_user.to_dict()
        self.assertIn('email', model_dict)
        self.assertIn('password', model_dict)
        self.assertIn('first_name', model_dict)
        self.assertIn('last_name', model_dict)

    def test_str_representation(self):
        """
        Test if the string representation of User contains expected information.
        """
        str_repr = str(self.test_user)
        self.assertIn("[User]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn(str(self.test_user.id), str_repr)

if __name__ == '__main__':
    unittest.main()

