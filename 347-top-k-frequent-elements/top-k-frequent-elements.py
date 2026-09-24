class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        pairs = []
        for key in freq:
            pairs.append((-freq[key], key))

        heapq.heapify(pairs)
        print(pairs)

        for _ in range(k):
            res.append(heapq.heappop(pairs)[1])

        return res