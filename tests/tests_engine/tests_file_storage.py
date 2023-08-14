#!/usr/bin/python3

import unittest
from models.file_storage import FileStorage
import json
import os

class TestFileStorage(unittest.TestCase):
        """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'FileStorage'
        self.value = FileStorage

    def setUp(self):
        """
        Set up a fresh instance of FileStorage for each test.
        """
        self.test_storage = FileStorage()

    def test_all_returns_dictionary(self):
        """
        Test if the 'all' method returns a dictionary.
        """
        result = self.test_storage.all()
        self.assertIsInstance(result, dict)

    def test_new_sets_in_objects(self):
        """
        Test if the 'new' method sets the object in __objects.
        """
        dummy_object = type('DummyObject', (object,), {'id': 'test_id'})()
        self.test_storage.new(dummy_object)
        self.assertIn('DummyObject.test_id', self.test_storage.all())

    def test_save_serializes_to_file(self):
        """
        Test if the 'save' method serializes __objects to the JSON file.
        """
        dummy_object = type('DummyObject', (object,), {'id': 'test_id'})()
        self.test_storage.new(dummy_object)
        self.test_storage.save()

        with open(self.test_storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertIn('DummyObject.test_id', data)

    def test_load_previous_data(self):
        """
        Test if the 'load_previous_data' method reloads stored objects.
        """
        dummy_object = type('DummyObject', (object,), {'id': 'test_id'})()
        self.test_storage.new(dummy_object)
        self.test_storage.save()

        new_storage = FileStorage()
        new_storage.load_previous_data()
        self.assertIn('DummyObject.test_id', new_storage.all())

    def test_attributes_returns_dictionary(self):
        """
        Test if the 'attributes' method returns a dictionary.
        """
        result = self.test_storage.attributes()
        self.assertIsInstance(result, dict)

    def test_classes_returns_dictionary(self):
        """
        Test if the 'classes' method returns a dictionary.
        """
        result = self.test_storage.classes()
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
