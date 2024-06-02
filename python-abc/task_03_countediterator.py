#!/usr/bin/python3
"""Define a class CountedIterator that extends the built-in
    iterator obtained from the iter function"""


class CountedIterator:
    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the current count of items iterated."""
        return self.counter

    def __next__(self):
        """Return the next item and increment the counter.
            Raise StopIteration if no items left."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Return the iterator itself."""
        return self
