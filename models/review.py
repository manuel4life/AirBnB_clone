#!/usr/bin/python3
""" This is the Review class module """

from models.base_model import BaseModel


class Review(BaseModel):
    """ The Review class """

    place_id = ""
    user_id = ""
    text = ""
