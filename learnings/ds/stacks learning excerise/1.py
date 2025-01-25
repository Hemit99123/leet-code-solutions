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


def reverse_string(text):
    stack = Stack()

    reverse = ""

    for char in text:
        stack.push(char)

    
    for _ in range(stack.size()):
        new_char = stack.peek()

        reverse += new_char

        stack.pop()
    
    return reverse


print(reverse_string("We will conquere COVID-19"))
# 91-DIVOC ereuqnoc lliw eW
