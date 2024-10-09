# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        if str1 + str2 != str2 + str1:
            return ''
        if len1 == len2:
            return str1
        if len1 > len2:
            return self.gcdOfStrings(str1[len2:], str2)
        return self.gcdOfStrings(str1, str2[len1:])
