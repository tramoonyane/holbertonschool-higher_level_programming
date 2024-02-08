#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class with area and integer_validator methods.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message
        'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value.

        Args:
            - name (str): Name of the value.
            - value: Value to be validated.

        Raises:
            - TypeError: If the value is not an integer.
            - ValueError: If the value is less than or equal to 0.

        You can assume name is always a string.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
