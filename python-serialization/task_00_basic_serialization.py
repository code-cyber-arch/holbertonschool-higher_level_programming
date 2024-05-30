#!/usr/bin/env python3
"""basic serialization module that adds the functionality to serialize a
    Python dictionary to a JSON file and deserialize the JSON file to
    recreate the Python Dictionary."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The filename of the output JSON file.
        If the output file already exists, it should be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        # Use json.dumps to serialize the dictionary and write to the file
        file.write(json.dumps(data))


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file to recreate a
        Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data from the
        file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Use json.loads to deserialize the JSON data from the file
        return json.loads(file.read())
