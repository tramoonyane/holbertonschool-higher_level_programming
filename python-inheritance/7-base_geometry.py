#!/usr/bin/python3

class BaseGeometry:
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")


   
