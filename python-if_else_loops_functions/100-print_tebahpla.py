#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        diff = 32
    else:
        diff = 0
    print('{}'.format(chr(i - diff)), end='')

# Add a newline at the end for better readability
print()
