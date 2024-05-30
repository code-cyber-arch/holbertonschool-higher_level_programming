#!/usr/bin/python3
""" class Student that defines a student"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student
            instance based on specified attributes.

        Args:
            attrs (list, optional): A list of attribute names to
            include in the result.

        Returns:
            dict: A dictionary representation of the instance.
        """
        if isinstance(attrs, list):
            return {attr: getattr(self, attr, None) for
                    attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__
