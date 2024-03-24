#!/usr/bin/python3

"""module containing file storage class for 
serialisation and deserialisation all of my
objects
"""


import json
from models.base_model import BaseModel


class FileStorage():
    """file storage class with methods that ensure 
    persistance of my objects"""

    __file_path = "file.json"

    __objects = {}

    def_classes = {"BaseModel": BaseModel}


    def all(self):
        """returns dictionary of __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects, the structure of the key, value
        dictionary i.e <obj class name>.id = obj"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serialises objects to json file in the path 
        indicted above i.e __file_path"""

        pyObjs = {}

        for key, value in FileStorage.__objects.items():

            pyObjs[key] = value.to_dict()

            with open(FileStorage.__file_path, "w", encoding='utf-8') as jstr:

                json.dump(pyObjs, jstr)


    def reload(self):
        """deserialises the json file to __objects, if file path 
        doesn't exists ensure no exception is raised"""

        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as jfile:

                deserialised_data = json.load(jfile)

                for objVals in deserialised.values():

                    clsName = objVals['__class__']

                    clsObj = self.def_Classes[clsName]

                    self.new(clsObj(**objVals))

        except Exception:
            pass
