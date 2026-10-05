class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        math_operators = {'+','*','-','/'}
        for element in tokens:
            if element in math_operators: # if encounter operator pop the last 2 elements, apply operator and push back to the stack
                second_operand = stack.pop()
                first_operand = stack.pop()
                result = 0
                if element == '+':
                    result = first_operand + second_operand
                if element == '*':
                    result = first_operand * second_operand
                if element == '-':
                    result = first_operand - second_operand
                if element == '/':
                    result = first_operand / second_operand

                stack.append(int(result))
            else:
                stack.append(int(element))

        return stack[0] # result is the only element left in stack   
        