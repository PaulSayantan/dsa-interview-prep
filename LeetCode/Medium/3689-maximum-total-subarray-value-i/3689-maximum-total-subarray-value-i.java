class Solution {
    public long maxTotalValue(int[] nums, int k) {
        /*
         * Calculates the maximum possible total value by choosing k subarrays.
         * * Approach:
         * 1. Because the problem statement explicitly mentions subarrays can overlap 
         * and be chosen more than once, we don't need complex dynamic programming.
         * 2. The best strategy is purely greedy: find the single maximum possible 
         * subarray value, and reuse it 'k' times.
         * 3. The maximum subarray value achievable is (global_max - global_min).
         * 4. To avoid integer overflow during multiplication, the difference must 
         * be explicitly cast to a 'long'.
         * * Complexity:
         * - Time Complexity: O(n) - One pass loop through the array.
         * - Space Complexity: O(1) - Constant memory allocation.
         */
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        
        // Single pass to find both limits efficiently without stream overhead
        for (int num : nums) {
            if (num > max) max = num;
            if (num < min) min = num;
        }
        
        // Safe casting to prevent overflow
        return (long)(max - min) * k;
    }
}