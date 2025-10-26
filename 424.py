# 424. Longest Repeating Character Replacement
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
# Example 1:
# Input: s = "XYYX", k = 2
# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.
# Example 2:
# Input: s = "AAABABB", k = 1
# Output: 5

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        count = {}
        l = 0

        for r in range(len(s)):
          count[s[r]] = count.get(s[r], 0) + 1                  # count freq of each char
          while (r - l + 1) - max(count.values()) > k:          # while window not valid
              count[s[l]] -= 1                                  # decrement frequency of leftmost char
              l += 1                                            # move up left pointer
          maxLen = max(maxLen, r - l + 1)                       # update maximum depending on size of current window
        return maxLen
