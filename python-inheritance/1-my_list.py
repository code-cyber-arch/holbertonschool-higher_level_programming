#!/usr/bin/python3
"""Define a class."""

class MyList(list):

    def print_sorted(self):

        """print list."""
        sorted_list = sorted(self)
        print(sorted_list)
