#!/usr/bin/python3

from tests.test_models.test_base_model import test_basemodel
from models.user import User

class TestUser(test_basemodel):
    """
    Test class for the User model.

    This class contains unit tests for the attributes of the User model,
    such as first_name, last_name, email, and password.
    """

    def __init__(self, *args, **kwargs):
        """Initialize TestUser class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.user_class = User

    def test_first_name(self):
        """
        Test the first_name attribute of the User.

        This test checks whether the first_name attribute of a User instance
        is of type str.
        """
        new_user = self.user_class()
        self.assertEqual(type(new_user.first_name), str)

    def test_last_name(self):
        """
        Test the last_name attribute of the User.

        This test checks whether the last_name attribute of a User instance
        is of type str.
        """
        new_user = self.user_class()
        self.assertEqual(type(new_user.last_name), str)

    def test_email(self):
        """
        Test the email attribute of the User.

        This test checks whether the email attribute of a User instance
        is of type str.
        """
        new_user = self.user_class()
        self.assertEqual(type(new_user.email), str)

    def test_password(self):
        """
        Test the password attribute of the User.

        This test checks whether the password attribute of a User instance
        is of type str.
        """
        new_user = self.user_class()
        self.assertEqual(type(new_user.password), str)


# Example of how to use the TestUser class:
if __name__ == "__main__":
    test_user_instance = TestUser()
    test_user_instance.test_first_name()
    test_user_instance.test_last_name()
    test_user_instance.test_email()
    test_user_instance.test_password()
