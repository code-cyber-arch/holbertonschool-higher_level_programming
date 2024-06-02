#!/usr/bin/python3
"""Define a class to override list methods for verbose output."""


class VerboseList(list):
    """A list subclass that prints messages when modifying the list."""

    def __init_subclass__(cls):
        """Ensure base class's __init_subclass__ is called."""
        return super().__init_subclass__()

    def append(self, value):
        """
        Add an item to the end of the list with a message.

        Parameters:
        value (any): The item to be added to the list.
        """
        print(f"Added [{value}] to the list.")
        return super().append(value)

    def extend(self, values):
        """
        Extend the list with items from an iterable with a message.

        Parameters:
        values (iterable): Elements to add to the list.
        """
        print(f"Extended the list with [{len(values)}] items.")
        return super().extend(values)

    def remove(self, value):
        """
        Remove the first occurrence of a value from the list with a message.

        Parameters:
        value (any): The value to remove from the list.
        """
        print(f"Removed [{value}] from the list.")
        return super().remove(value)

    def pop(self, index=-1):
        """
        Remove and return the item at the given index with a message.

        Parameters:
        index (int): The index of the item to remove. Default is
            -1 (last item).

        Returns:
        any: The removed item.
        """
        value = self[index] if -len(self) <= index < len(self) else None
        result = super().pop(index)
        if value is not None:
            print(f"Popped [{value}] from the list.")
        return result
