#!/usr/bin/python3
"""Define a class"""


class SwimMixin:
    """Mixin class to add swimming capability."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying capability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon that can swim and fly."""
    def roar(self):
        print("The dragon roars!")
