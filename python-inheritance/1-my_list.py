#!/usr/bin/python3
"""Define a class."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """print list."""
        print(sorted(self))
