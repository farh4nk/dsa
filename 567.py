# 567. Permutation in String
# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
# Both strings only contain lowercase letters.
# Example 1:
# Input: s1 = "abc", s2 = "lecabee"
# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".
# Example 2:
# Input: s1 = "abc", s2 = "lecaabee"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}
        for char in s1:
            perm[char] = perm.get(char, 0) + 1
        l = 0
        window = {}
        for c in s2[0:len(s1)]:
            window[c] = window.get(c, 0) + 1
        for r in range(len(s1), len(s2)):
            if window.items() == perm.items():
                return True
            window[s2[r]] = window.get(s2[r], 0) + 1
            window[s2[l]] -= 1
            if (window[s2[l]]) == 0:
                window.pop(s2[l])
            l += 1
        return window == perm
