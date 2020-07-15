"""
@author: Abhishek Khatri
Description: This class defines all the methods used to create and manipulate 
stack.
"""

class Stack():
    def __init__(self):
        self.elements = []
    
    #Adding element to stack
    def push(self, element):
        self.elements.append(element)
    
    #removing an element from stack
    def pop(self):
        return self.elements.pop()
    
    #Check if stack is empty
    def is_empty(self):
        return self.elements == []
    
    #Look for the last element of stack
    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
    
    #Give all the elements currently in stack
    def get_stack(self):
        return self.elements