class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            # Check if the stack is not empty before accessing stack[-1]
            if stack and (
                (item == ")" and stack[-1] == "(") or
                (item == "]" and stack[-1] == "[") or
                (item == "}" and stack[-1] == "{")
            ):
                stack.pop()
            else:
                stack.append(item)
        
        # If the stack is empty, all brackets were matched
        return len(stack) == 0
