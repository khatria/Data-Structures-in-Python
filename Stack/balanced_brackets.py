'''
This code uses stack class to determine if brackets are balanced or not
'''
from stack import Stack

def match_brackets(bracket1, bracket2):
    if bracket1 == '(' and bracket2 == ')':
        return True
    elif bracket1 == '[' and bracket2 == ']':
        return True
    elif bracket1 == '{' and bracket2 == '}':
        return True
    else:
        return False
    
def check_brackets(s):
    mystack = Stack()
    is_balanced = True
    index = 0
    while index < len(s) and is_balanced:
        bracket = s[index]
       # print(bracket)
        if bracket in '({[':
            mystack.push(bracket)
        else:
            if mystack.is_empty():
                is_balanced = False
            else:
                top = mystack.pop()
               # print(top)
                if not match_brackets(top, bracket):
                    is_balanced = False
        index += 1
        
    if mystack.is_empty() and is_balanced:
        return True
    else:
        return False

print(check_brackets('()'))