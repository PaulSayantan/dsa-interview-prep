class Solution {
    /**
     * 🧠 PATTERN: Two-Pointer Overwrite (Reader / Writer)
     * 
     * 📌 Core Insights:
     * 1. The input array is already SORTED: all identical numbers are adjacent.
     * 2. We want at most K duplicates (here K = 2).
     * 3. Instead of counting duplicates with a separate counter, we inspect the
     *    element already written K steps behind (`nums[write - 2]`).
     * 4. Because the array is sorted, if `num > nums[write - 2]`, it is impossible
     *    for `num` to be a 3rd duplicate of that number.
     * 
     * ⏱️ Time Complexity:  O(n) - Single pass through all elements.
     * 💾 Space Complexity: O(1) - Modified in-place without extra memory.
     */
    public int removeDuplicates(int[] nums) {
        // 'write' tracks the index where the next valid element should be placed.
        int write = 0;
        
        // 'num' acts as the fast reader pointer scanning through every element.
        for (int num : nums) {
            // Condition 1: Always keep the first 2 elements (write < 2).
            // Condition 2: If we have 2+ elements, only accept 'num' if it is
            //              strictly greater than the element placed 2 spots back.
            if (write < 2 || num > nums[write - 2]) {
                nums[write] = num; // Place valid element at current write pointer
                write++;           // Advance the write boundary
            }
            // If the condition fails, 'num' is a duplicate we already have 2 of,
            // so we simply skip writing it.
        }
        
        // 'write' represents both the length of the valid prefix and the return value.
        return write;
    }
}