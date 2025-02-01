'''
4. Next Greater Element
Problem: For each element in an array, find the next greater element to the right. If there is no greater element, return -1.
Example:
Input: [4, 5, 2, 10, 8]
Output: [5, 10, 10, -1, -1]
'''


elements = [4,5,2,10,8]

ans = [-1] * len(elements)
stack = []

for index in range(len(elements)):

    element = elements[index]

    if (stack):
        while (stack and element > elements[stack[-1]]):
            ans[stack[-1]] = element
            stack.pop()    
    stack.append(index)

print(ans)