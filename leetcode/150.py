# 150. Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:
# Input: tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(float(op2) / op1))
            else:
                stack.append(int(t))
        return stack[-1]



