# Python Data Structures: Lists and Tuples

## Lists

### What are lists and how to use them

In Python, a list is a versatile and mutable data structure that allows you to store and manipulate a collection of items. Lists are created using square brackets and can contain elements of different data types.

```python
my_list = [1, 2, 3, 'hello', True]

Differences and Similarities between Strings and Lists
Strings and lists share some similarities as both are sequences, but they have key differences. Strings are immutable, meaning their elements cannot be changed after creation, while lists are mutable.

Most Common Methods of Lists and How to Use Them
Python provides a variety of methods for manipulating lists. Some common methods include append(), extend(), pop(), remove(), index(), and sort(). Here's an example:

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

Using Lists as Stacks and Queues
Lists can be used as stacks (Last In, First Out) and queues (First In, First Out) using the append() and pop() methods. Stacks:

stack = []
stack.append(1)
stack.append(2)
item = stack.pop()

Queues using collections.deque:

from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
item = queue.popleft()

List Comprehensions
List comprehensions provide a concise way to create lists. They are more readable and efficient compared to traditional for-loops.

squares = [x**2 for x in range(5)]

Tuples
What are Tuples and How to Use Them
A tuple is an immutable sequence in Python, created using parentheses. Tuples are similar to lists but cannot be modified after creation.

my_tuple = (1, 2, 'hello')

When to Use Tuples Versus Lists
Use tuples when you want to create an immutable, ordered sequence. Lists are preferred for mutable, dynamic sequences.

What is a Sequence
A sequence is an ordered collection of items. Both lists and tuples are examples of sequences.

Tuple Packing
Tuple packing is the process of creating a tuple by placing multiple values inside parentheses.

my_tuple = 1, 'hello', 3.14

Sequence Unpacking
Sequence unpacking allows you to assign values from a sequence to multiple variables in a single line.

x, y, z = my_tuple

The del Statement and How to Use It
The del statement is used to delete items from a list or elements from a tuple.

my_list = [1, 2, 3]
del my_list[1]


Feel free to customize this README.md content according to your specific project and requirements.

Author: Thetele Ramoonyane


Feel free to use this content as a starting point and modify it further based on your needs.
