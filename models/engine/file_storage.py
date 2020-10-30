#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initializes a FileStorage instance
        """

    def all(self):
        """
        Returns _objects dictionary
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = type(obj).__name__+ "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
        except:
            pass
