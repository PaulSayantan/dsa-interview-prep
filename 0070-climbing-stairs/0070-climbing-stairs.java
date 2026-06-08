class Solution {
    /**
     * Calculates the distinct ways to climb to the top of a staircase with `n` steps.
     * * Intuition: 
     * Since ways(n) = ways(n-1) + ways(n-2), we only ever need the last two calculated 
     * values to find the next one.
     * * Approach: Bottom-Up Dynamic Programming (Space Optimized)
     * Iterates from step 2 to `n`, keeping track of the last two results using 
     * constant variables instead of an array.
     * * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public int climbStairs(int n) {
        // Base cases
        if (n <= 1) {
            return 1;
        }
        
        // Represents ways to reach (k-2)
        int prev2 = 1; 
        // Represents ways to reach (k-1)
        int prev1 = 1; 
        
        // Loop iteratively to calculate ways for each step up to n
        for (int i = 2; i <= n; i++) {
            // Current step is the sum of the last two
            int current = prev1 + prev2;
            
            // Shift values forward for the next iteration
            prev2 = prev1;
            prev1 = current;
        }
        
        // prev1 holds the final result
        return prev1;
    }
}