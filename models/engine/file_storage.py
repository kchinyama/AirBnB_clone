#!/usr/bin/python3

"""module containing file storage class for 
serialisation and deserialisation all of my
objects
"""

import json
#from models.base_model import BaseModel

class FileStorage():
    """file storage class with methods that ensure 
    persistance of my objects"""

    __file_path = "file.json"

    __objects = {}


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

        pyDict = {}

        for key, value in FileStorage.__objects.items():

            pyDict[key] = value.to_dict()

            with open(FileStorage.__file_path, "w", encoding='utf-8') as jstr:
                json.dump(pyDict, jstr)

    def reload(self):
        """deserializes the JSON file to __objects, if file path exists
        otherwise, does nothing"""

        from models.base_model import BaseModel

        defined_classes = {"BaseModel": BaseModel}

        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as jfile:
                deserialed_data = json.load(jfile)

                for objVals in deserialed_data.values():

                    clsname = objVals["__class__"]

                    clsObj = defined_classes[clsname]

                    self.new(clsObj(**objVals))

        except FileNotFoundError:
            pass
