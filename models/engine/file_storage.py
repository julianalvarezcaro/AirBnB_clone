#!/usr/bin/python3
"""
Module for FileStorage class
"""
from models.base_model import BaseModel
import json
import os.path


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns _objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        dic = {}
        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dic, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                deseria = json.load(file)
            for key, value in deseria.items():
                objd = eval(value["__class__"])(**value)
                FileStorage.__objects[key] = objd
