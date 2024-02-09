#!/usr/bin/python3

def class_to_json(obj):
    """
    Converts an instance of a class to a dictionary description
    with simple data structures for JSON serialization.

    Parameters:
    obj (object): An instance of a Class with serializable attributes.

    Returns:
    dict: A dictionary containing the serializable attributes of the object.
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object is not an instance of a class")

    serializable_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_data[key] = value

    return serializable_data
