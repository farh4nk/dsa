class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        substring = ''
        indices = {}

        for i in range(len(s)):
            c = s[i]

            if c not in substring:
                substring += c
            else:
                maxLen = max(len(substring), maxLen)
                substring = s[indices[c]+1:i+1]
            indices[c] = i
        maxLen = max(len(substring), maxLen)
        return maxLen

