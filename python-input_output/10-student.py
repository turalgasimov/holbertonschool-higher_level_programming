#!/usr/bin/python3
"""This module defines a student class."""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if all(isinstance(item, str) for item in attrs):
            obj_dict = {}
            for _ in attrs:
                obj_dict[_] = getattr(self, _)
        else:
            return self.__dict__
