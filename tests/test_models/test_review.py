#!/usr/bin/python3
"""Unittesting module for Review class
"""
import models
from models.review import Review
import os
import unittest


class TestReview(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.review.__doc__)

        #  Class check
        self.assertIsNotNone(Review.__doc__)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/review.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/review.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/review.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if reviewlInstance is an instance
        of review()
        """
        reviewInstance = Review()
        self.assertIsInstance(reviewInstance, Review)

if __name__ == '__main__':
    unittest.main()
