class Solution {
    /**
     * Removes duplicate elements from a sorted array in-place such that each unique element 
     * appears only once. The relative order of the elements is kept the same.
     *
     * @param nums The input array of integers, sorted in non-decreasing order.
     * @return The total count of unique elements in the array.
     */
    public int removeDuplicates(int[] nums) {
        
        // EDGE CASE 1: Array of size 1
        // If the array contains exactly one element, there are no duplicates to remove.
        // The item at the 0th index is already at its correct, sorted position.
        if (nums.length == 1) {
            return 1;
        }
        
        // EDGE CASE 2: Array of size 2
        // If the array contains exactly two elements, we evaluate them directly.
        if (nums.length == 2) {
            // If both elements are identical, there is only 1 unique element.
            if (nums[0] == nums[1]) {
                return 1;
            }
            // If they are different, both elements are unique.
            return 2;
        }
        
        /*
         * TWO-POINTER APPROACH:
         * 'i' acts as the "slow" pointer. It tracks the index of the most recently confirmed unique element.
         * 'j' acts as the "fast" pointer. It iterates through the array to discover new unique elements.
         */
        int i = 0;
        
        // Start iteration from the 1st index (j = 1) up to the end of the array.
        for (int j = 1; j < nums.length; j++) {
            
            // Since the array is sorted, any element strictly greater than the last unique 
            // element (nums[i]) means we have discovered a brand new unique number.
            if (nums[i] < nums[j]) {
                
                // Copy the newly found unique element into the position immediately 
                // following the last confirmed unique element.
                nums[i + 1] = nums[j];
                
                // Move the slow pointer forward to officially register the newly placed element.
                i++;
            }
        }
        
        // 'i' represents the 0-based index of the last unique element placed in the array. 
        // We return 'i + 1' to convert this index into a 1-based count/length of unique elements.
        return i + 1;
    }
}