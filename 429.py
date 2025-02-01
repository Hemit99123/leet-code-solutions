'''
4. Next Greater Element
Problem: For each element in an array, find the next greater element to the right. If there is no greater element, return -1.
Example:
Input: [4, 5, 2, 10, 8]
Output: [5, 10, 10, -1, -1]
'''

# O(n) or O(2n) -> monotonic stacks approach

print("MONOTONIC STACKS:")

elements = input().split()

ans = ['-1'] * len(elements)
stack = []

for index in range(len(elements)):

    element = int(elements[index])

    if (stack):
        while (stack and element > int(elements[stack[-1]])):
            ans[stack[-1]] = str(element)
            stack.pop()    
    stack.append(index)

print(" ".join(ans))

# O(n^2) -> brute force approach

print("BRUTE FORCE:")

elements = list(map(int, input().split()))  # Convert input to integers

ans = ['-1'] * len(elements)

for i in range(len(elements)):
    for y in range(i + 1, len(elements)):  # Look ahead
        if elements[y] > elements[i]:  # Compare as integers
            ans[i] = str(elements[y])  # Convert result to string
            break

print(" ".join(ans))

