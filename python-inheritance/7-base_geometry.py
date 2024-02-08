#!/usr/bin/python3

class BaseGeometry:
    """Defines a base geometry class."""

    def integer_validator(self, name, value):
        """Validates that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
