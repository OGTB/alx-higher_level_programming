#!/bin/usr/python3
"""Base module"""


import json
import csv
import turtle
from math import sqrt
from os import path


class Base:
    """class Base"""
    __nb_objetcs = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objetcs
