#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF-8) and return the
        number of characters written.

    Args:
        filename: The name of the file to write to.
        text: The string to write to the file.

    Returns:
        The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
