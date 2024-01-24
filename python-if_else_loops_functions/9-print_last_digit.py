#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    print(last_digit)
    return last_digit

# Test the function
result = print_last_digit(12345)
# The function prints: 5
print("Last digit:", result)
