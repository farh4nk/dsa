# 20. Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
# Example 1:
# Input: s = "[]"
# Output: true
# Example 2:
# Input: s = "([{}])"
# Output: true
# Example 3:
# Input: s = "[(])"
# Output: false
# Explanation: The brackets are not closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      pairs = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
      }

      for c in s:
        if c in pairs:
          if stack and stack[-1] == pairs[c]:
            stack.pop()
          else:
            return False
        else:
          stack.append(c)
      return stack == []
