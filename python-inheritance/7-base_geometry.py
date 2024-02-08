python
#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class with methods for area calculation and integer validation.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if the given value is an integer and greater than 0.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer with a custom message.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
# Examples for doctests:
if __name__ == "__main__":
    bg = BaseGeometry()  # Create an instance of BaseGeometry for testing

    # Example 1
    bg.integer_validator("age", {3, 4})
    # Expected: Raises a TypeError with the message "age must be an integer"

    # Example 2
    bg.integer_validator("age", None)
    # Expected: Raises a TypeError with the message "age must be an integer"
