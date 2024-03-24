#!/usr/bin/python3

"""
BaseModel module that will define all the common attributes
and methods for all classes
"""


from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage

class BaseModel():
    """BaseModel class that contains all methods and attributes
    of our instances"""

    def __init__(self, *args, **kwargs):
        """our constructor for each instance that will be created"""

        if kwargs:
            del kwargs['__class__']

            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dTimeObj = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                            )
                    setattr(self, key, dTimeObj)

                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

            storage.new()

           # self.updated_at = datetime.now()

    def __str__(self):
        """human readable rep of all my instances"""

        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """updates time stamp on updated_at time stamp"""
        
        updated_at = datetime.now

        storage.save()

    def to_dict(self):
        """returns key, value pairs of the __dict__ of instance"""

        pyDictObjs = {}

        pyDictObjs['__class__'] = self.__class__.__name__

        for key, value in self.__dict__.items():

            if isinstance(value, datetime):
                pyDictObjs[key] = datetime.now().isoformat()

            else:
                pyDictObjs[key] = value

        return pyDictObjs
