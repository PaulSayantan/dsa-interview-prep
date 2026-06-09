class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum possible total value by choosing k subarrays.
        
        KEY INSIGHT:
        The problem states that "the exact same subarray can be chosen more than once." 
        To maximize our final total, we don't need a complex splitting strategy. 
        Instead, we should find the single absolute best subarray that yields the 
        highest possible value, and greedily choose that exact same subarray 'k' times.
        
        The maximum value of any subarray is bounded by the difference between 
        the highest and lowest numbers in the entire array (global_max - global_min). 
        Thus, the entire problem boils down to: (global_max - global_min) * k.
        
        Complexity:
        - Time Complexity: O(n) because we find the max and min in a single pass.
        - Space Complexity: O(1) auxiliary space.
        """
        # Find the global maximum and minimum in O(n) time
        global_max = max(nums)
        global_min = min(nums)
        
        # Replicating the absolute best subarray 'k' times
        return (global_max - global_min) * k