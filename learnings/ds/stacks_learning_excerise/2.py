from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def is_balanced(text):
    stack = Stack()

    valid_paranthesis = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in text:

        if (char in valid_paranthesis and stack.size() != 0):

            opening_paranthesis = valid_paranthesis[char]
            last_char = stack.peek()

            if (last_char == opening_paranthesis):
                stack.pop()
                continue
        
        if (char in "[]{}()"):
            stack.push(char)

    return stack.size() == 0

# Testing for correctness in my program
print(is_balanced("({a+b})"))   
print(is_balanced("))((a+b}{"))   
print(is_balanced("((a+b))"))     
print(is_balanced("))"))        
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))