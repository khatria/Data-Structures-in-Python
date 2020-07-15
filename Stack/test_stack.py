"""
This script checks all the methods implemented using stack class.
"""
from stack import Stack

#creating stack class instance
my_stack = Stack()
print(my_stack.get_stack())

#Adding element to stack
my_stack.push('A')
my_stack.push('B')
print(my_stack.get_stack())

my_stack.push('C')
print(my_stack.get_stack())

#removing element from stack
my_stack.pop()
print(my_stack.get_stack())

#Checking last element and checking if the stack is empty or not
print(my_stack.peek())
print(my_stack.is_empty())

