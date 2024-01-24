#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of the character is between the ASCII values of 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')

# Test the function
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('1'))  # False
