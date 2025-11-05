class KthLargest:

    def __init__(self, k: int, nums: List[int]): # min heap of size k
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # keep popping until you get k largest elements
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: # pop if size exceeds
            heapq.heappop(self.minHeap)
        return self.minHeap[0] # return element at the top of the heap
        # which will be the kth largest element b/c we popped all other smaller elements
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)