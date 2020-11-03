#!/usr/bin/python3
"""Unittesting module for BaseModel class
"""
import models
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.base_model.__doc__)

        #  Class check
        self.assertIsNotNone(BaseModel.__doc__)

        # Methods check
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
