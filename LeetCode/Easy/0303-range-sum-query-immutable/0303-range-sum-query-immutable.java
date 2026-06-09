/**
 * Problem: Range Sum Query - Immutable
 * Approach: Prefix Sum Array
 * * Thought Process:
 * If we calculate the sum from scratch for every `sumRange` query, it would take O(N) time 
 * per query. Since there can be up to 10^4 queries, this would result in a Time Limit Exceeded (TLE).
 * * Instead, we can precompute the cumulative sums. 
 * Let prefixSum[i] be the sum of elements from nums[0] to nums[i].
 * Once we have this, any range sum from 'left' to 'right' can be found mathematically in O(1) time:
 * Sum(left to right) = Sum(0 to right) - Sum(0 to left - 1)
 */
class NumArray {
    
    // Array to store the running cumulative sums
    private int[] prefixSum;

    /**
     * Initializes the object and precomputes the prefix sum array.
     * Time Complexity: O(N)
     * Space Complexity: O(N)
     */
    public NumArray(int[] nums) {
        int size = nums.length;
        this.prefixSum = new int[size];
        
        // Base case: The sum up to index 0 is simply the first element itself.
        this.prefixSum[0] = nums[0];
        
        // Iteratively build the cumulative sum.
        // The sum up to index 'i' is the sum up to index 'i-1' plus the current element at 'i'.
        for (int i = 1; i < size; i++) {
            this.prefixSum[i] = this.prefixSum[i - 1] + nums[i];
        }
    }

    /**
     * Returns the sum of elements between indices left and right inclusive.
     * Time Complexity: O(1)
     */
    public int sumRange(int left, int right) {
        // Edge Case: If left is 0, we want the sum from the very beginning of the array.
        // This is exactly what prefixSum[right] holds, so we don't need to subtract anything.
        if (left == 0) {
            return this.prefixSum[right];
        }
        
        // General Case: Subtract the elements we DON'T want from the total sum up to 'right'.
        // We want the sum starting at 'left', so we discard everything up to 'left - 1'.
        return this.prefixSum[right] - this.prefixSum[left - 1];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */