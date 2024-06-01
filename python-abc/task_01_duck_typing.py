#!/usr/bin/python3
"""Abstract Method"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Defines an abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a new circle.

        Args:
            radius (float): The radius of the circle.
        """
        if radius < 0:
            self.__radius = abs(radius)
        else:
            self.__radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a new rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of a shape.

    Args:
        shape (Shape): The shape object.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
