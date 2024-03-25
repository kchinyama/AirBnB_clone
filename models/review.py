#!/usr/bin/python3

"""user module that holds the reviews class
attributes"""


from models.base_model import BaseModel


class Review(BaseModel):
    """the review class with attributes, inheriting from
    BaseModel"""
    
    place_id = ""
    user_id = ""
    text = ""
