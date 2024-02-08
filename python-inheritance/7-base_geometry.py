class BaseGeometry:
    """
    Base class for geometric shapes.

    Methods:
    - area(): Placeholder for calculating the area. Subclasses must implement this method.
    - integer_validator(name, value): Validates the 'value' parameter as an integer.
      Raises TypeError if 'name' is not a string or 'value' is not an integer.
      Raises ValueError if 'value' is less than or equal to 0.
    """
    def area(self):
        """Placeholder for calculating the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the 'value' parameter as an integer."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
