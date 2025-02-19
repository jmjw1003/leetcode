class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(left_operand + right_operand)
            elif token == "-":
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(left_operand - right_operand)
            elif token == "*":
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(left_operand * right_operand)
            elif token == "/":
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(int(left_operand / right_operand))
            else:
                stack.append(int(token))
        return stack[0]