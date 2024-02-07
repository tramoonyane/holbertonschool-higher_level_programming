#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a class that inherited from a_class; otherwise, False.
    """
    # Get the class of the object
    obj_class = type(obj)

    # Check if the object's class is a subclass of the specified class
    return issubclass(obj_class, a_class)
