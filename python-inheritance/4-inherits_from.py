#!/usr/bin/python3
"""Define a Function"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    Otherwise, returns False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
