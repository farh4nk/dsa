# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = min(strs, key=len) # get the shortest word to avoid indexing errors
        strs.remove(shortest)
        for i in range(len(shortest)):
            for str in strs:
                if (shortest[i] != str[i]):
                    return prefix
            prefix += shortest[i]
        return prefix  
