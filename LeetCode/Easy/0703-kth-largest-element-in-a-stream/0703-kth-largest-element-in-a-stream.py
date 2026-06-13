import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # 1. Transform the initial list into a min-heap
        heapq.heapify(self.heap)
        
        # 2. Pop the smallest elements until only the 'k' largest remain
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Push the new value into the heap
        heapq.heappush(self.heap, val)
        
        # If the heap size exceeds k, pop the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of the min-heap is always the kth largest element
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)