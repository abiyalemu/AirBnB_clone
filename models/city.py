#!/usr/bin/python
""" holds class city """
from models.base_model import BaseModel


class City(BaseModel):
    """ represenation of city """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, *kwargs)
        
