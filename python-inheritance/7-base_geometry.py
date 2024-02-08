#!/usr/bin/python3

class BaseGeometry:
    """Defines a base geometry class.

    Methods:
        integer_validator(self, name, value): Validates that the value is a positive integer.
        area(self): Placeholder method for calculating the area.

    """

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """Placeholder method for calculating the area.

        Raises:
            Exception: Indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")
