#!/usr/bin/python3
"""This module defines a student class."""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            obj_dict = {}
            for _ in attrs:
                if _ not in self.__dict__.keys():
                    continue
                obj_dict[_] = getattr(self, _)
            return obj_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            self.k = v
