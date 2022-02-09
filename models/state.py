#!/usr/bin/python
""" hold class state """
from models.base_model import BaseModel


class State(BaseModel):
    """represenation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
        
