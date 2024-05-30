#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
