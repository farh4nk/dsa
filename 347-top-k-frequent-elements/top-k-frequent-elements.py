class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums) + 1)]
        res = []
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for n,c in freq.items():
            counts[c].append(n)
        for i in range(len(counts)-1, 0, -1):
            for n in counts[i]:
                res.append(n)
            if len(res) == k:
                return res
        