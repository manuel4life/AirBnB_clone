#!/usr/bin/python3
""" This the file storage module
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ The file storage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the __objects dictionary """
        # response = FileStorage.reload(self)
        # print("{}".format(response))
        return FileStorage.__objects

    def new(self, obj):
        """ adds new objects to the __objects """

        class_name = obj.__class__.__name__
        id = obj.id
        key = "{}.{}".format(class_name, id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to a JSON file """

        objects_dict = {key: FileStorage.__objects[key].to_dict()
                        for key in FileStorage.__objects.keys()}

        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(objects_dict, fp)

    def reload(self):
        """ deserializes a JSON file to __objects """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fp:

                dict_returned = json.load(fp)

                for obj in dict_returned.values():
                    class_name = obj["__class__"]
                    # del obj["__class__"]
                    self.new(eval(class_name)(**obj))
                return
