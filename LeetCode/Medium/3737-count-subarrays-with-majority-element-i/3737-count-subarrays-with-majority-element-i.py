class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """
        Thought Process:
        The problem asks us to find all subarrays where a specific `target` element 
        appears strictly more than half the time. Looking at the constraints, 
        nums.length is at most 1000. An O(n^2) brute-force algorithm will take 
        roughly 1,000,000 operations, which easily passes within the standard time limits.
        Therefore, we can check every possible subarray.

        Intuition:
        Instead of counting the exact frequencies of all elements in every subarray 
        (which would be slow and require extra space), we only care about the balance 
        between our `target` element and *all other* elements combined. 
        If we treat the `target` as +1 and any other number as -1, a subarray has the 
        `target` as its majority element if and only if the sum of these values is strictly greater than 0.

        Approach:
        1. Initialize a `count` variable to keep track of the valid subarrays.
        2. Use a nested loop to generate all possible subarrays. The outer loop `i` 
           sets the starting index of the subarray.
        3. For each starting index `i`, initialize a `majority` counter to 0.
        4. The inner loop `j` expands the subarray one element at a time to the right.
        5. For each new element nums[j], adjust the `majority` counter (+1 if it's 
           the target, -1 if it's not).
        6. If `majority` > 0, it means the target appears strictly more than half 
           the time in the current subarray nums[i..j], so we increment our `count`.
        """
        n = len(nums)
        count = 0  # To store the total number of valid subarrays
        
        # i represents the starting index of our current subarray
        for i in range(n):
            majority = 0  # Tracks the net balance of 'target' vs 'non-target' elements
            
            # j represents the ending index of our current subarray
            for j in range(i, n):
                # If we see the target, it helps our majority score
                if nums[j] == target:
                    majority += 1
                # If we see any other number, it hurts our majority score
                else:
                    majority -= 1
                
                # If the score is positive, the target outnumbers all other elements combined
                # meaning it strictly takes up more than half the subarray length
                if majority > 0:
                    count += 1
                    
        return count