#!/usr/bin/python3

"""
BaseModel module that will define all the common attributes
and methods for all classes
"""


from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel class that contains all methods and attributes
    of our instances"""

    def __init__(self):
        """our constructor for each instance that will be created"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """human readable rep of all my instances"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates time stamp on updated_at time stamp"""

        updated_at = datetime.now

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
