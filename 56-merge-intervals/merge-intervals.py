class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        res.append(sorted_intervals[0])

        for i in range(1, len(intervals)):
            curr = sorted_intervals[i]
            prev = res[-1]

            if curr[0] <= prev[1]:
                res[-1][1] = max(curr[1], res[-1][1])
            else:
                res.append(curr)

        return res