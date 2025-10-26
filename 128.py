# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            longest = 1
            s = set(nums)
            for n in s:
                curr = 1
                if n-1 not in s:
                    while n+1 in s:
                        n += 1
                        curr += 1
                longest = max(longest, curr)
            return longest
        else:
            return 0


            

