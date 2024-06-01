#!/usr/bin/python3
"""Abstract Method"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Defines an abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Make a sound.

        This method should be implemented by subclasses to return
        the sound made by the animal.
        """
        pass


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the sound made by a dog.

        Returns:
            str: The sound "Bark".
        """
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the sound made by a cat.

        Returns:
            str: The sound "Meow".
        """
        return "Meow"
