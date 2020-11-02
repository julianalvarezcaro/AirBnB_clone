#!/usr/bin/python3
"""
Module for BaseModel class
"""
from datetime import datetime
import models  # Variable created on models.__init__.py
import uuid


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
            formaTi = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, formaTi))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dic = self.__dict__.copy()  # Clarify later
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
