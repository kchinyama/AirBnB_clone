#!/usr/bin/python3

"""user module that holds the city class
attributes"""


from models.base_model import BaseModel


class City(BaseModel):
    """the city class with attributes, inheriting from
    BaseModel"""
    
    state_id = ""
    name = ""
