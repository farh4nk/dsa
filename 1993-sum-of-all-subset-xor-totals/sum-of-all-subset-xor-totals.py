class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xortotal(arr):
            xor = 0
            for n in arr:
                xor = xor ^ n
            return xor


        subsets = []
        curr = []
        def backtrack(i):
            if i >= len(nums):
                subsets.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i+1)

            curr.pop()
            backtrack(i+1)

            return subsets
        backtrack(0)
        
        res = 0
        for s in subsets:
            res += xortotal(s)
        
        return res