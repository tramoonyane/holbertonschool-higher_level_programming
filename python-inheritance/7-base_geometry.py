#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class represents the base geometry operations.

    Public Methods:
        - area(self): Raises an Exception with the message "area() is not implemented."
        - integer_validator(self, name, value): Validates the given value as an integer and checks if it is greater than 0.
    """

    def area(self):
        """
        Calculate the area of the geometry. This method is not implemented and raises an Exception.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer and check if it is greater than 0.

        Args:
            name (str): A string representing the name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer, raises a TypeError with the message "<name> must be an integer."
            ValueError: If the value is less than or equal to 0, raises a ValueError with the message "<name> must be greater than 0."
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


# Run tests using `python3 -m doctest ./tests/7-base_geometry.txt`
