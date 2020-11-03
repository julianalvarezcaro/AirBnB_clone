#!/usr/bin/python3
"""Unittesting module for User class
"""
import models
from models.user import User
import os
import unittest


class TestUser(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.user.__doc__)

        #  Class check
        self.assertIsNotNone(User.__doc__)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/user.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/user.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/user.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if userlInstance is an instance
        of user()
        """
        userInstance = User()
        self.assertIsInstance(userInstance, User)

if __name__ == '__main__':
    unittest.main()
