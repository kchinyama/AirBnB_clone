#!/usr/bin/python3

"""user module that holds the state class
attributes"""


from models.base_model import BaseModel


class State(BaseModel):
    """the state class with attributes, iheriting from
    BaseModel"""

    name = ""
