#!/usr/bin/python3

class BaseGeometry:
    def integer_validator(self, name, value):
        if not isinstance(value, (int, bool)):
            raise TypeError(f"{name} must be an integer or boolean")

        if isinstance(value, int) and value <= 0:
            raise ValueError(f"{name} must be an integer greater than 0")

        if isinstance(value, bool):
            raise TypeError(f"{name} must be a boolean, not an integer")

        # Additional conditions can be added here as needed
        # ...

    def area(self):
        raise Exception("area() is not implemented")
