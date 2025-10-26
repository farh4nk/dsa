# 49. Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
# Example 3:
# Input: strs = [""]
# Output: [[""]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord("a")] += 1 # each word gets a 26-int list
            res[tuple(count)].append(str) # add the string to list corresponding with the count array
        return res.values()
            
