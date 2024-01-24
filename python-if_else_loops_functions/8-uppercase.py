#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        # Check if the character is lowercase using ASCII values
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase character to uppercase using ASCII manipulation
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char

        print("{}".format(uppercase_char), end='')

    # Print a newline after processing the entire string
    print()
