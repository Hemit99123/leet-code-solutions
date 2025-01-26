# Learnt that .pop() method removes last item BUT also returns it. good for other stack problems 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-/*"

        for token in tokens:
            if (token in operators):
                number2 = int(stack.pop())
                number1 = int(stack.pop())
                result = 0

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
            
        return int(stack[0])
