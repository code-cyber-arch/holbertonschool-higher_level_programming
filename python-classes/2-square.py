#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0) -> None:
        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError('size must be an integer')
