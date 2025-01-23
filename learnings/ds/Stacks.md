# Stacks: What is it?

A stack is a data structure that keeps track of different items (like a list). However, it follows a specific pattern, known as **LAST IN, FIRST OUT (LIFO)**.

### What does this pattern even mean?
It means that the last item added (the most recent item) will be the first one to be removed.

### When to use a stack?
Stacks are ideal when you want to remove or edit the most recent item within a collection of such items. Consider whether your scenario requires you to work with the last item added. If so, a stack is a great fit!

### Common methods for stacks:
- **Push**: Adds an item to the stack.
- **Pop**: Removes the last item from the stack.
- **Peek**: Returns the last item added without removing it.

### How to implement a stack in Python:
In Python, a simple list can be used to implement a stack. The key difference is how you interact with the list.

```python
stack = []

# Add item (push)
stack.append(1)

# Remove last item (pop)
stack.pop()

# View last item (peek)
last_item = stack[-1] if stack else None  # Check if stack is not empty before peeking
```

This code demonstrates how to use a Python list as a stack:
- **append()** adds items to the stack (push).
- **pop()** removes the most recent item (pop).
- **stack[-1]** allows you to peek at the last item added.
