#!/usr/bin/python3
"""Unittesting module for State class
"""
import models
from models.state import State
import os
import unittest


class TestStatel(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.state.__doc__)

        #  Class check
        self.assertIsNotNone(State.__doc__)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/state.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/state.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/state.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if StatelInstance is an instance
        of State()
        """
        StateInstance = State()
        self.assertIsInstance(StateInstance, State)

if __name__ == '__main__':
    unittest.main()
