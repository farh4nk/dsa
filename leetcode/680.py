# 680. Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Example 1:
# Input: s = "aba"
# Output: true
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
# Input: s = "abc"
# Output: false

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True


        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)
            
        return True
