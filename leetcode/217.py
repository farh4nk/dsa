# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = False;
        for i, num in enumerate(nums):
            for inner_num in nums[i+1:]:
                if num == inner_num:
                    hasDuplicate = True
                    break
        return hasDuplicate


# This brute force solution is O(n^2). Optimized solution would use a Hash Set, and would be O(n).
