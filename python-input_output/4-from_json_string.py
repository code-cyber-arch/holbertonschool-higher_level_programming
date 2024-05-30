#!/usr/bin/python3
"""function that returns an object (Python data structure) represented by
    a JSON string"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str: The JSON string to convert to a Python object.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
