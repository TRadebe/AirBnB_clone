#!/usr/bin/python3

import unittest
from models.user import User
from tests.test_models.test_base_model import TestBasemodel

class TestUser(TestBasemodel):
    """
    Test class for the User model.

    This class contains unit tests for the attributes of the User model,
    such as first_name, last_name, email, and password.
    """

    def test_first_name(self):
        """
        Test the first_name attribute of the User.

        This test checks whether the first_name attribute of a User instance
        is of type str.
        """
        new_user = User()
        self.assertEqual(type(new_user.first_name), str)

    def test_last_name(self):
        """
        Test the last_name attribute of the User.

        This test checks whether the last_name attribute of a User instance
        is of type str.
        """
        new_user = User()
        self.assertEqual(type(new_user.last_name), str)
