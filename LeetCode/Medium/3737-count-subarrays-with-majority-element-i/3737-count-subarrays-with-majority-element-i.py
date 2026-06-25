class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """
        O(n) Time | O(n) Space Approach Using Prefix Sums & Dynamic Frequencies
        """
        n = len(nums)
        # We need an array to store the frequencies of prefix sums we have seen.
        # Since the prefix sum can range from -n to +n, we use an array of size 2n + 2.
        # We'll use 'n' as our "zero" offset so we don't have to deal with negative indices.
        freq = [0] * (2 * n + 2)
        offset = n 
        
        running_sum = 0
        # We start by having seen a prefix sum of 0 exactly once (the empty prefix before the array starts)
        freq[offset + 0] = 1 
        
        smaller_count = 0  # Tracks how many previous prefix sums are STRICTLY LESS than the current running_sum
        total_subarrays = 0
        
        for num in nums:
            if num == target:
                # Our sum is going up by 1.
                # Therefore, any prefix sum that was exactly equal to our OLD running sum 
                # is now strictly smaller than our NEW running sum.
                smaller_count += freq[offset + running_sum]
                running_sum += 1
            else:
                # Our sum is going down by 1.
                # Therefore, any prefix sum that is exactly equal to our NEW running sum 
                # is no longer strictly smaller than it. We must subtract its frequency.
                running_sum -= 1
                smaller_count -= freq[offset + running_sum]
            
            # The current 'smaller_count' represents the exact number of valid starting 
            # indices for the current ending index 'j'. We add it to our total.
            total_subarrays += smaller_count
            
            # Finally, record that we have seen this new running_sum one more time.
            freq[offset + running_sum] += 1
            
        return total_subarrays