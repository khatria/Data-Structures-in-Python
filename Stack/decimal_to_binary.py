'''
This converts a decimal to binary using stack 
'''
from stack import Stack

mystack = Stack()
def decimal_to_binary(num):
    while num > 0:
        mystack.push(num%2)
        num = num // 2
   # print(mystack.get_stack())
    binary_num = "" 
    while not mystack.is_empty():
        binary_num += str(mystack.pop())
    return binary_num

print(decimal_to_binary(25))