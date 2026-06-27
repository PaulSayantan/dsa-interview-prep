class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm approach
        
        # Step 1: Initialize variables
        # 'maxi' stores the highest subarray sum encountered so far. 
        # It's initialized to a very small number so the first valid sum will overwrite it.
        maxi = -10001
        
        # 'add' acts as our running sum tracking the current contiguous subarray.
        add = 0
        
        # Step 2: Iterate through the array element by element
        for i in range(len(nums)):
            
            # Continuously add the current element to the ongoing subarray sum.
            add += nums[i]
            
            # Step 3: Update the maximum sum
            # If our newly calculated running sum is greater than the recorded 'maxi',
            # we've found a new maximum, so we update 'maxi'.
            if add > maxi:
                maxi = add
                
            # Step 4: The Core Intuition (Drop Negative Sums)
            # If our running sum drops below zero, it mathematically guarantees that 
            # carrying it forward will only REDUCE the sum of any future subarray.
            # Because it will only hamper our future subset sums, we drop the current 
            # subarray entirely by resetting our running sum ('add') to 0.
            if add < 0:
                add = 0
                
        # Return the maximum contiguous subarray sum found.
        return maxi