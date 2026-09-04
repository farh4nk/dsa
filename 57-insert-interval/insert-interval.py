class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]
        
        def merge(intervals):
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

        new = []
        for i in range(len(intervals)):
            inserted = False

            if not inserted and intervals[i][0] > newInterval[0]:
                new.append(newInterval)
                inserted = True

            new.append(intervals[i])

        if len(new) == len(intervals):
            new.append(newInterval)

        return merge(new)