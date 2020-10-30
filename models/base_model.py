#!/usr/bin/python3
"""
Module for BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel class

    Defines all common attributes/methods for other classes:

    Instance attributes:
        Public:
            - id
            - created_at
            - updated_at
    Instance methods:
        Public:
            - save(self)
            - to_dict(self)
    Special method:
        - __init__(self)
        - __str__(self)
    """
    def __init__(self, *_args, **kwargs):
        """
        Initializes an instance of BaseModel class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key not in ["__class__", "created_at", "updated_at"]:
                    self.__dict__[key] = value
            self.__dict__['created_at'] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__['updated_at'] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of an instance
        """
        return "[" + self.__class__.__name__ + "] " \
            + "(" + str(self.id) + ") " + str(self.__dict__)

    def save(self):
        """
        Updates the public instance update_at with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
