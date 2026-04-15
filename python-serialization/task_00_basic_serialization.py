#!/usr/bin/python3
"""This module adds the functionality
to serialize a Python dictionary to a JSON file
and deserialize the JSON file to recreate the Python Dictionary."""
import json

def serialize_and_save_to_file(data, filename):
    """Serialize and save to file."""
    with open(filename, "w") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """Load and deserialize."""
    with open(filename, "r") as f:
        data = f.read()
        return json.loads(data)
