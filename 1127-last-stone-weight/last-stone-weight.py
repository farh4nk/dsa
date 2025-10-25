class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # negate all numbers to make a pseudo max-heap
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones) # get two largest stones

            if y > x:
                heapq.heappush(stones, x-y) # adding x-y to heap since values are negative

        return -stones[0] if stones else 0 # negate back to original form
