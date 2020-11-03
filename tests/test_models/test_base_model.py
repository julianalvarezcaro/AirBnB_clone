#!/usr/bin/python3
"""Unittesting module for BaseModel class
"""
import models
from models.base_model import BaseModel
import os
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

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if BaseModelInstance is an instance
        of BaseModel()
        """
        BaseModelInstance = BaseModel()
        self.assertIsInstance(BaseModelInstance, BaseModel)

    def test_different_id(self):
        """Method that check if each instance that is created has
        a unique id
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)

if __name__ == '__main__':
    unittest.main()
