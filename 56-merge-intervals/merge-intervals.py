class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0]) # special syntax for sorting by start val
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end) # the end of the previous intervals becomes the larger value
            else:
                res.append([start, end])

        return res