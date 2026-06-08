class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the distinct ways to climb to the top of a staircase with `n` steps.
        
        Intuition:
        To reach a given stair `k`, you must have come from either:
        1. The stair just below it (k-1), by taking a 1-step.
        2. The stair two levels below it (k-2), by taking a 2-step.
        Therefore, the total number of ways to reach stair `k` is simply the sum 
        of the ways to reach stair `k-1` and the ways to reach stair `k-2`. 
        This fundamentally follows the Fibonacci sequence logic.

        Approach: Top-Down Dynamic Programming (Memoization)
        We use a recursive function to work backwards from `n`. To prevent the 
        exponential time complexity of a pure recursive Fibonacci solution, we 
        store (memoize) previously calculated results in a list.
        
        Time Complexity: O(n) - We calculate the answer for each step exactly once.
        Space Complexity: O(n) - Due to the recursion stack and the `memo` array.
        """
        
        # Initialize a memoization array of size n+1 with -1 to represent uncalculated states.
        memo = [-1] * (n + 1)
        
        def stairs(k):
            # Base Cases: 
            # 0 steps: 1 way (do nothing)
            # 1 step: 1 way (take 1 step)
            if k <= 1: 
                return 1
            
            # If the result for this step has already been calculated, return it from the cache.
            if memo[k] != -1: 
                return memo[k]
            
            # Recursive Step: Calculate ways for k-1 and k-2, sum them, and store in the cache.
            memo[k] = stairs(k-1) + stairs(k-2)
            
            return memo[k]
            
        # Start the recursion from the top step.
        return stairs(n)