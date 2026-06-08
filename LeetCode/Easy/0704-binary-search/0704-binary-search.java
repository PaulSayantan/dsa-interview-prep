class Solution {
    /**
     * Intuition:
     * Binary search mimics looking up a word in a physical dictionary. Instead of 
     * flipping through pages one by one, you open it in the middle. Depending on 
     * alphabetical order, you eliminate either the entire front half or back half of 
     * the book. We apply this exact divide-and-conquer strategy to the sorted array.
     * * Approach:
     * 1. Set boundaries: 'low' at 0, 'high' at nums.length - 1.
     * 2. Iterate while low <= high to ensure every possible candidate index is checked.
     * 3. Compute 'mid = low + (high - low) / 2'. In Java, writing '(low + high) / 2' 
     * can cause an integer overflow bug if the sum exceeds Integer.MAX_VALUE.
     * 4. Perform three-way branching logic based on the comparison of nums[mid] and target.
     * 5. Adjust the pointers safely past 'mid' since 'mid' has already been evaluated.
     * * Complexity Analysis:
     * - Time Complexity: O(log n) -> Max iterations bounded by the logarithm of array size.
     * - Space Complexity: O(1)   -> Performed purely in-place.
     */
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        
        while (low <= high) {
            // Prevents overflow compared to (low + high) / 2
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return mid; // Target found
            } else if (nums[mid] < target) {
                low = mid + 1; // Discard left half
            } else {
                high = mid - 1; // Discard right half
            }
        }
        
        return -1; // Target does not exist
    }
}