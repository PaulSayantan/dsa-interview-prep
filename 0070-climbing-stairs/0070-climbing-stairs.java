class Solution {
    /**
     * Calculates the distinct ways to climb to the top of a staircase with `n` steps.
     * * Intuition: 
     * The total ways to reach step `k` is the sum of ways to reach `k-1` and `k-2`.
     * * Approach: Top-Down Dynamic Programming (Memoization)
     * Uses a recursive helper function and caches results in an array to avoid redundant work.
     * * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public int climbStairs(int n) {
        // Initialize memoization array. Default values will be 0 in Java.
        int[] memo = new int[n + 1];
        return stairs(n, memo);
    }
    
    private int stairs(int k, int[] memo) {
        // Base Cases
        if (k <= 1) {
            return 1;
        }
        
        // Return cached result if already computed (greater than 0)
        if (memo[k] > 0) {
            return memo[k];
        }
        
        // Recursive calculation and caching
        memo[k] = stairs(k - 1, memo) + stairs(k - 2, memo);
        
        return memo[k];
    }
}