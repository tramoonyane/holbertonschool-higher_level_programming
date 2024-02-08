#!/usr/bin/python3

#!/usr/bin/python3
"""
The ``7-base_geometry`` module
"""

class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        Not implemented method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the input value as an integer.

        Args:
            name (str): The name associated with the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
