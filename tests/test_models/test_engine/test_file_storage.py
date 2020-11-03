#!/usr/bin/python3
"""Unittest module for FileStorage
"""
import models
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.engine.file_storage.__doc__)

        #  Class check
        self.assertIsNotNone(FileStorage.__doc__)

        # Methods check
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.__str__.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if FileStorageInstance is an instance
        of FileStorage()
        """
        FileStorageInstance = FileStorage()
        self.assertIsInstance(FileStorageInstance, FileStorage)

    def test_different_id(self):
        """Method that check if each instance that is created has
        a unique id
        """
        instance1 = FileStorage()
        instance2 = FileStorage()
        self.assertNotEqual(instance1, instance2)

if __name__ == '__main__':
    unittest.main()
