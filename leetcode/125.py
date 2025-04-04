# Valid Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
# Example 2:
# Input: s = "tab a cat"
# Output: false
# Explanation: "tabacat" is not a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = ''
        for c in s:
            if c.isalnum():
                raw += c
        raw = raw.lower()
        l = 0
        r = len(raw) - 1
        while l < r:
            if raw[l] != raw[r]:
                return False
            l +=1
            r -= 1
        return True
