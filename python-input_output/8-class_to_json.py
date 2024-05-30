#!/usr/bin/python3
"""function that returns the dictionary description with
    simple data structure"""


def class_to_json(obj):
    """Return the dictionary description with simple data
        structure for JSON serialization of an object.

    Args:
        obj: The object to convert to a dictionary.

    Returns:
        A dictionary representation of the object's attributes.
    """
    return obj.__dict__
