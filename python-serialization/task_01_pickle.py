#!/usr/bin/python3
"""serialize and deserialize custom Python objects using the pickle module"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to the specified file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from the specified file."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"An error occurred during deserialization: {e}")
            return None
