#!/usr/bin/python3
""" subclass defines a user """

from models.base_model import BaseModel


class User(BaseModel):
    """subclass to define the User and its attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    age = 0
