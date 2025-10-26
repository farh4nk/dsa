# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.
# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        arr = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for key in counts:
            arr[counts[key]].append(key)
        
        res = []
        pointer = len(arr) - 1
        for i in range(pointer, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
