# ### Conceptual Breakdown
# 
# Core Algorithmic Patterns:
# - Prefix Sum
# - Hash Map (Frequency Map)
#
# Mental Intuition & Logic:
# - A brute-force approach checking every subarray would take O(N^2) time, which is too slow 
#   for the given constraint N = 20,000.
# - A sliding window approach is invalid here. Because the array can contain negative numbers 
#   (-1000 <= nums[i] <= 1000), expanding the window doesn't guarantee an increasing sum, and 
#   shrinking it doesn't guarantee a decreasing sum.
# - We optimize to O(N) by using the mathematical properties of a Prefix Sum. The sum of a 
#   subarray from index `i` to `j` is: `prefix_sum[j] - prefix_sum[i-1]`.
# - If we want this subarray sum to equal `k`, the equation is: 
#   `prefix_sum[j] - prefix_sum[i-1] = k`.
# - By algebraically rearranging this, we get: `prefix_sum[i-1] = prefix_sum[j] - k`.
# - Therefore, as we iterate through the array maintaining a running total (`prefix_sum[j]`), 
#   we simply need to check if we have previously encountered a prefix sum equal to 
#   `current_sum - k`. If we have, every time we saw that prefix sum represents a valid subarray.

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Calculates the total number of continuous subarrays whose sum equals exactly k.
        
        Args:
            nums (List[int]): The input array of integers, which may contain negative numbers.
            k (int): The target sum for the subarrays.
            
        Returns:
            int: The total count of valid subarrays.
            
        Complexity:
            Time: O(N) where N is the length of nums. The array is traversed exactly once.
            Space: O(N) to store the prefix sum frequencies in the hash map. In the worst case,
                   all prefix sums are distinct.
        """
        count = 0
        current_sum = 0
        
        # Initialize with {0: 1} to handle the case where a valid subarray starts from index 0.
        # This implies that a prefix sum of 0 has occurred exactly once before we even start.
        prefix_sums = {0: 1} 
        
        for num in nums:
            current_sum += num
            
            # If the difference between current_sum and k exists in our history map,
            # we found valid subarrays. Add the frequency of that past prefix sum.
            target = current_sum - k
            if target in prefix_sums:
                count += prefix_sums[target]
                
            # Record the current prefix sum into our history map for future iterations
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count

# ### Reusable Patterns & Key Takeaways
# 
# 1. Negative Numbers Neutralize Sliding Windows: When an array contains both positive and 
#    negative integers, two-pointer or sliding window techniques fail because the monotonic 
#    property of the sum is broken. Always pivot to Prefix Sum arrays + Hash Maps in these scenarios.
#
# 2. The `Current - Target = Previous` Equation: This algebraic rearrangement 
#    (`prefix_sum[j] - k = prefix_sum[i-1]`) is the fundamental cornerstone of many O(N) 
#    contiguous subarray problems.
#
# 3. Frequency Maps Over Sets: We use a hash dictionary instead of a hash set because the array 
#    contains zeros and negative numbers. This means the running prefix sum can fluctuate and hit 
#    the same value multiple times. We must add the *frequency* of the past prefix sum to our 
#    count, not just increment by 1.
#
# 4. Base Case Initialization: Always initialize the prefix sum map with `{0: 1}`. Without this, 
#    any valid subarray that perfectly matches `k` starting from the very first element (index 0) 
#    will be skipped.