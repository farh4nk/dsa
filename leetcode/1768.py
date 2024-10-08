# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        p1, p2 = 0, 0
        while (p1 < len(word1) and p2 < len(word2)):
            result += word1[p1]
            result += word2[p1]
            p1 +=1
            p2 +=1
        result += word1[p1:]
        result += word2[p2:]
        return result
            

