#!/usr/bin/python3
"""Unittesting module for Amenity class
"""
import models
from models.amenity import Amenity
import os
import unittest


class TestAmenity(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.amenity.__doc__)

        #  Class check
        self.assertIsNotNone(Amenity.__doc__)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if amenitylInstance is an instance
        of amenity()
        """
        amenityInstance = Amenity()
        self.assertIsInstance(amenityInstance, Amenity)

if __name__ == '__main__':
    unittest.main()
