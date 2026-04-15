#!/usr/bin/python3
"""This module is for serializatino tasks."""
import csv
import json


def convert_csv_to_json(filename):
    """converts csv to json"""

    try:
        with open(filename, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True

    except Exception:
        return False
