#!/usr/bin/python3
"""Read a text file (UTF-8) """


def read_file(filename=""):
    """Read a text file (UTF-8) and print its contents to stdout.

    Args:
        filename: The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
