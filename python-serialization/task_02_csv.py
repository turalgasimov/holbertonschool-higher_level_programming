#!/usr/bin/python3
"""This module is for serializatino tasks."""
import csv
import json


def convert_csv_to_json(filename):
    """converts csv to json"""

    data = {}

    try:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                data.update(row)
        
        with open("data.json", "w") as f:
            json.dump(data, "data.json")

    except Exception:
        return False
