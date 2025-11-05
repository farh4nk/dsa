class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p):
                return (p[0]**2 + p[1]**2) ** 0.5

        distances = [] # heap of tuples: (distance, point)
        for point in points:
            heapq.heappush(distances, (distance(point), point) )

        res = []
        while k > 0 and distances:
            res.append(heapq.heappop(distances)[1])
            k -= 1
        return res
        