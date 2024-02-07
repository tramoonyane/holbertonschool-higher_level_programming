#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class

# Example usage:
# obj = SomeClass()
# result = is_same_class(obj, SomeClass)
# print(result)
