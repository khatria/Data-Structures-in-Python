"""
Given a string, this code generates the reverse of the string
"""
from stack import Stack

def reverse_string(s):
    my_stack = Stack()
    [my_stack.push(s[i]) for i in range(len(s))]
    reverse_string = ''
    while not my_stack.is_empty():
        reverse_string += my_stack.pop()
        
    return reverse_string

print(reverse_string('irtahk kehsihba'))