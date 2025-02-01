'''
4. Next Greater Element
Problem: For each element in an array, find the next greater element to the right. If there is no greater element, return -1.
Example:
Input: [4, 5, 2, 10, 8]
Output: [5, 10, 10, -1, -1]
'''


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