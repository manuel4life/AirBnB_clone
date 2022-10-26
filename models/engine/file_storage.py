#!/usr/bin/python3
""" This the file storage module
"""

import os
import json


class FileStorage:
    """ The file storage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the __objects dictionary """

        return FileStorage.__objects

    def new(self, obj):
        """ adds new objects to the __objects """

        class_name = obj.__class__.__name__
        id = obj.id
        key = "{}.{}".format(class_name, id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to a JSON file """

        e_objects = FileStorage.__objects
        e_objects_dict = {key: e_objects[key].to_dict() for key in e_objects.keys()}
        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(e_objects_dict, fp)

    def reload(self):
        """ deserializes a JSON file to __objects """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path ) as fp:
                res = json.load(fp)
                return res
