class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for token in tokens:
            if (token in "+-/*"):
                number2 = int(stack.pop())
                number1 = int(stack.pop())

                match token:
                    case "+":
                        result = number1 + number2
                    case "-":
                        result = number1 - number2
                    case "/":
                        result = number1 / number2
                    case "*":
                        result = number1 * number2

                stack.append(result)
            else:
                stack.append(token)
        # this is to check if tokens does not have an operand. in that case
        # the stack would have one number which would be in a string datastructure        
        if isinstance(stack[-1], str):
            return int(stack[-1])
        else:
            return int(result)
