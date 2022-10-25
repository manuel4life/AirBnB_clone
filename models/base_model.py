#!/usr/bin/python3
""" base class module """

from datetime import datetime
import uuid

class BaseModel:
    """The base class for the AirBnB project"""

    def __init__(self, ):
        """ Init function """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
    def __str__(self):
        """ Default str method """

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ update the updated_at with current time """

        self.updated_at = datetime.today()

    def to_dict(self):
        """ returns a dict of the key/value of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
