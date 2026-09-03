class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        res = 0

        # sort in descending order
        costs.sort(key=lambda x: x[1] - x[0], reverse=True)
        print(costs)

        # send the first n people to city A
        for i in range(n):
            res += costs[i][0]

        # send the rest to city B
        for j in range(n, 2*n):
            res += costs[j][1]

        return res
