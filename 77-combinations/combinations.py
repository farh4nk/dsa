class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        subsets = []
        curr = []
        def backtrack(i):
            if i >= n:
                subsets.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i+1)

            curr.pop()
            backtrack(i+1)

        backtrack(0)

        res = []
        for s in subsets:
            if len(s) == k:
                res.append(s)

        return res