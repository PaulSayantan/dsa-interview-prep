class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Check if left child exists and is greater than root
            if left < n and nums[left] > nums[largest]:
                largest = left
                
            # Check if right child exists and is greater than largest so far
            if right < n and nums[right] > nums[largest]:
                largest = right
                
            # Change root, if needed, and continue heapifying
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        n = len(nums)
        
        # Step 1: Build a maxheap. 
        # Start from the last non-leaf node and heapify each node up to the root.
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
            
        # Step 2: Extract elements one by one
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # Swap root (max) with end
            heapify(i, 0)                        # Heapify the reduced heap
            
        return nums