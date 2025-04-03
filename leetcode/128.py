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
        res = []
        i = 0
        while i < len(nums)-1:
            curr = nums[i]
            if nums[i+1] == curr+1:
                res.append(curr)
                curr = nums[i+1]
            i += 1
        return len(res)
