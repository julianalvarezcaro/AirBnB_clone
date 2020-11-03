#!/usr/bin/python3
"""Unittesting module for Place class
"""
import models
from models.place import Place
import os
import unittest


class TestPlace(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.place.__doc__)

        #  Class check
        self.assertIsNotNone(Place.__doc__)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/place.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/place.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/place.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if placelInstance is an instance
        of place()
        """
        placeInstance = Place()
        self.assertIsInstance(placeInstance, Place)

if __name__ == '__main__':
    unittest.main()
