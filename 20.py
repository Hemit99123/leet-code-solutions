class Solution:
    def isValid(self, s: str) -> bool:

        # This is our stack which is a DS we will use to retrieve the last element and use that 
        # to validate the closing parentheses
        
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
        # The len() function itself returns a boolean so therefore no need for any if/else statements to return a statement
        return len(stack) == 0
