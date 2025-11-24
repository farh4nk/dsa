class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # iterate through intervals, 3 cases:
        # 1. newInterval comes before current interval
        # 2. newInterval comes after current interval
        # 3. newInterval overlaps with current interval

        for i, interval in enumerate(intervals):
            # case 1
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            # case 2
            elif newInterval[0] > interval[1]:
                res.append(interval)
            # case 3
            else:
                merged = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
                newInterval = merged
        res.append(newInterval)

        return res