class BaseGeometry:
    """Defines a base geometry class."""

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """Placeholder method for calculating the area."""
        raise Exception("area() is not implemented")
