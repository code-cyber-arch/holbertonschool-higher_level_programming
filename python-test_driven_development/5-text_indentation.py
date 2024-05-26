#!/usr/bin/python3
"""Defines a square-printing function."""


def text_indentation(text):
    """Print  a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
        text (str):
    Raises:
        TypeError: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1
    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
