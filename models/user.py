#!/usr/bin/python3
"""
    class User that inherits from BaseModel:

    models/user.py
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string

    Update FileStorage to manage correctly serialization
    and deserialization of User.

    Update your command interpreter (console.py) to
    allow show, create, destroy, update and all used with
    User.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

