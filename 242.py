# 242. Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# nput: s = "racecar", t = "carrace"
# Output: true
# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        for char in s:
            s_letters.update({char: s.count(char)})
        for char in t:
            t_letters.update({char: t.count(char)})

        return (s_letters.items() == t_letters.items())
        
