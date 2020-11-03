#!/usr/bin/python3
"""Unittesting module for City class
"""
import models
from models.city import City
import os
import unittest


class TestCity(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.city.__doc__)

        #  Class check
        self.assertIsNotNone(City.__doc__)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/city.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/city.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/city.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if citylInstance is an instance
        of city()
        """
        cityInstance = City()
        self.assertIsInstance(cityInstance, City)

if __name__ == '__main__':
    unittest.main()
