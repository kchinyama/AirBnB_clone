#!/usr/bin/python3

"""user module that holds the amenity class
attributes"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """the amenity class with attributes, inheriting from
    BaseModel"""
    
    name = ""
