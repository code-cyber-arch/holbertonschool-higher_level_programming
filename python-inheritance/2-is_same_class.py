#!/usr/bin/python3
"""Function that returns True/False if obj is a type of a_class"""


def is_same_class(obj, a_class):
    """Function that returns True/False if obj is a type of a_class

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
