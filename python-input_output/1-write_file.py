#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return the
        number of characters written.

    Args:
        filename: The name of the file to write to.
        text: The string to write to the file.

    Returns:
        The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
