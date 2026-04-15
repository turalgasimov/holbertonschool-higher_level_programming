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
        print(
            f"Name: {self.name}\n"+
            f"Age: {self.age}\n"+
            f"Is Student: {self.is_student}"
        )

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                data = f.read()
                return pickle.loads(data)
        except FileNotFoundError:
            return None

obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()