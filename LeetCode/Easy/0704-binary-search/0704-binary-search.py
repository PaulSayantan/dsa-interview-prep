from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Intuition:
        If an array is already sorted, we don't need to scan it linearly. We can 
        leverage its sorted nature by checking the middle element. If the target 
        is smaller than the middle element, it must reside in the left half. If it's 
        larger, it must be in the right half. This allows us to discard half of the 
        remaining search space with every single comparison.
        
        Approach:
        1. Initialize two pointers: 'low' at index 0 and 'high' at the last index (n - 1).
        2. Loop while 'low' is less than or equal to 'high'. The '<=' is crucial because 
           when low == high, we are inspecting the final remaining element.
        3. Calculate the middle index 'mid' carefully to avoid potential overflow.
        4. If nums[mid] equals the target, return 'mid'.
        5. If nums[mid] is less than the target, narrow the search space to the right half (low = mid + 1).
        6. If nums[mid] is greater than the target, narrow the search space to the left half (high = mid - 1).
        7. If the loop exits without finding the target, return -1.
        
        Complexity Analysis:
        - Time Complexity: O(log n) -> The search space is halved at each step.
        - Space Complexity: O(1)   -> Only a few pointers are used; memory usage is constant.
        """
        low, high = 0, len(nums) - 1
        
        while low <= high:
            # Using low + (high - low) // 2 avoids potential integer overflow
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1