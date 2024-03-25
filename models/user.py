#!/usr/bin/python3

"""user module that holds the user class
attributes"""


from models.base_model import BaseModel


class User(BaseModel):
    """user class for users, inherits from the 
    BaseModel
    """

    email = ""
    password = ""
    firstname = ""
    last_name = ""
