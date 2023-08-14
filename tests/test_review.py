#!/usr/bin/python3

from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class TestReview(unittest.TestCase):
        """ """

        def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'Review'
        self.value = Review

    def setUp(self):
        """
        Set up a fresh instance of Review for each test.
        """
        self.test_review = Review()

    def test_subclass(self):
        """
        Test if Review is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_has_attributes(self):
        """
        Test if the Review instance has the expected attributes.
        """
        self.assertTrue(hasattr(self.test_review, 'place_id'))
        self.assertTrue(hasattr(self.test_review, 'user_id'))
        self.assertTrue(hasattr(self.test_review, 'text'))

    def test_id_is_valid_uuid(self):
        """
        Test if the 'id' attribute is a valid UUID.
        """
        self.assertTrue(UUID(self.test_review.id))

    def test_created_at_is_datetime(self):
        """
        Test if the 'created_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_review.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if the 'updated_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_review.updated_at, datetime.datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the 'to_dict' method returns a dictionary with expected keys.
        """
        model_dict = self.test_review.to_dict()
        self.assertIn('place_id', model_dict)
        self.assertIn('user_id', model_dict)
        self.assertIn('text', model_dict)

    def test_str_representation(self):
        """
        Test if the string representation of Review contains expected information.
        """
        str_repr = str(self.test_review)
        self.assertIn("[Review]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn(str(self.test_review.id), str_repr)

if __name__ == '__main__':
    unittest.main()
