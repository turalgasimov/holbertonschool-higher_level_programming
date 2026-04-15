#!/usr/bin/python3
"""This module uses pickle."""
import pickle


class CustomObject:
    """Class of custom object."""
    name = ""
    age = 0
    is_student = False

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student


    def serialize(self, filename):
        with open(filename, "wb") as f:
            f.write(pickle.dumps(self))


    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")


    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                data = f.read()
                return pickle.loads(data)
        except FileNotFoundError:
            return None
