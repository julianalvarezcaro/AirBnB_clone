#!/usr/bin/python3
"""Unittest module for FileStorage
"""
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittesting class
    """

    def test_docs(self):
        """Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(models.file_storage.__doc__)

        #  Class check
        self.assertIsNotNone(FileStorage.__doc__)

        # Methods check
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.__str__.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.to_dict.__doc__)