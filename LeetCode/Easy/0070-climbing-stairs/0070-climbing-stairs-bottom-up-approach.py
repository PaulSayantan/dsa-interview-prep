class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the distinct ways to climb to the top of a staircase with `n` steps.
        
        Intuition:
        Just like the memoization approach, the number of ways to reach step `n` is 
        the sum of the ways to reach `n-1` and `n-2`. 
        
        Approach: Bottom-Up Dynamic Programming (Space Optimized)
        Instead of building a full array of size `n` or using a recursion stack, we can 
        compute the steps iteratively starting from step 2 up to step `n`. We only keep 
        track of the previous two values using two variables (`prev1` and `prev2`), 
        updating them sequentially.
        
        Time Complexity: O(n) - We iterate through the loop roughly `n` times.
        Space Complexity: O(1) - We only use a few variables, requiring constant extra space.
        """
        
        # Base cases: If the staircase has 0 or 1 steps, there is only 1 way to climb it.
        if n <= 1:
            return 1
            
        # `prev2` represents ways to reach (k-2) -> initially step 0
        prev2 = 1 
        # `prev1` represents ways to reach (k-1) -> initially step 1
        prev1 = 1 
        
        # Iteratively calculate the ways to reach the current step `i`
        for i in range(2, n + 1):
            # The current step is the sum of the previous two steps
            current = prev1 + prev2
            
            # Shift the variables forward for the next iteration
            prev2 = prev1
            prev1 = current
            
        # `prev1` will hold the final answer for step `n` after the loop finishes
        return prev1