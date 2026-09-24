class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        res = set()
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        pairs = []
        for n in nums:
            pairs.append((-freq[n], n))

        heapq.heapify(pairs)
        print(pairs)

        while len(res) < k:
            res.add(heapq.heappop(pairs)[1])

        return list(res)