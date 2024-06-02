#!/usr/bin/python3
"""A class FlyingFish"""


class Fish:
    """
    A class representing a fish.
    """
    def swim(self):
        """Prints that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.
    """
    def fly(self):
        """Prints that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, inheriting from
        both Fish and Bird.
    """
    def fly(self):
        """Prints that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")
