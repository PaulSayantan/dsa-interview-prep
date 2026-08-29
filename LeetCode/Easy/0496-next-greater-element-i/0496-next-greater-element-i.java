/**
 * ============================================================================
 * PROBLEM: Next Greater Element I
 * ============================================================================
 * 
 * ### Conceptual Breakdown ###
 * 
 * 1. Core Algorithmic Patterns:
 *    - Monotonic Stack: Specifically, a strictly decreasing stack.
 *    - Hash Map: For O(1) element lookups to bridge the relationship 
 *      between the universal array (nums2) and the subset array (nums1).
 * 
 * 2. Mental Intuition & Logic:
 *    - The Brute Force approach checks every element to the right, taking 
 *      O(N * M) time. We want to avoid scanning the right side repeatedly.
 *    - The "Waiting Room" Concept: We iterate through `nums2` from left to right. 
 *      If we see a smaller number, we don't know its next greater element yet, 
 *      so we push it onto the stack. The stack acts as a waiting room for 
 *      elements that haven't found their next greater match.
 *    - The "Trigger": When we arrive at a number that is LARGER than the number 
 *      at the top of the stack, we have found the answer for that waiting element.
 *      Because a stack is Last-In, First-Out (LIFO), we resolve the most recently 
 *      seen smaller elements first.
 *    - We pop the resolved element and store the relationship `(Popped Element -> 
 *      Current Larger Element)` in a Hash Map.
 *    - Once `nums2` is fully processed, any elements left in the stack never 
 *      found a greater element to their right, so they implicitly map to -1.
 *    - Finally, we iterate through `nums1` and simply look up each element in 
 *      our populated Hash Map.
 */
class Solution {
    
    /**
     * Finds the next greater element for a subset of numbers.
     * 
     * @param nums1 The query array (a subset of nums2).
     * @param nums2 The reference array where we search for the next greater element.
     * @return An array containing the next greater element for each number in nums1.
     */
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // Map to store the next greater element for each number in nums2.
        // Key: The number | Value: Its next greater element
        Map<Integer, Integer> nextGreaterMap = new HashMap<>();
        
        // The monotonic decreasing stack acting as our "waiting room".
        // It stores the actual values from nums2, not indices.
        Deque<Integer> stack = new ArrayDeque<>();
        
        // Pass 1: Process the universal array (nums2) to build our mapping
        for (int currentNum : nums2) {
            // While the stack is not empty AND the current number is strictly greater 
            // than the number at the top of the stack...
            while (!stack.isEmpty() && currentNum > stack.peek()) {
                // We found the next greater element for the waiting number.
                // Pop it and record the relationship in the map.
                int waitingNum = stack.pop();
                nextGreaterMap.put(waitingNum, currentNum);
            }
            // Push the current number onto the stack to wait for its own greater element
            stack.push(currentNum);
        }
        
        // Pass 2: Resolve the queries for nums1 using the pre-computed map
        int[] result = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            // If the element exists in the map, return the mapped value.
            // If it doesn't (meaning it was left unresolved in the stack), return -1.
            result[i] = nextGreaterMap.getOrDefault(nums1[i], -1);
        }
        
        return result;
    }
}

/**
 * ============================================================================
 * ### Reusable Patterns & Key Takeaways ###
 * ============================================================================
 * 
 * 1. The "Next Greater/Smaller" Signal: 
 *    Any problem asking to find the "next greater", "next smaller", "previous 
 *    greater", or "previous smaller" element in an array is an immediate, 
 *    massive signal to use a Monotonic Stack.
 * 
 * 2. Subset Query Pattern:
 *    When dealing with a subset array (`nums1`) querying a universal array 
 *    (`nums2`), always pre-process the universal array first. Store the 
 *    computed relationships in a Hash Map. This decouples the processing logic 
 *    from the querying logic, reducing nested loops and turning query resolution 
 *    into an O(1) operation.
 * 
 * 3. Amortized Time Complexity:
 *    Even though there is a `while` loop inside the `for` loop during Pass 1, 
 *    the Time Complexity is strictly O(N + M). This is because every element in 
 *    `nums2` is pushed onto the stack exactly once and popped from the stack at 
 *    most once. The inner loop's operations amortize to O(1) per element.
 * 
 * 4. Space Complexity:
 *    O(M) auxiliary space, where M is the length of `nums2`. In the worst-case 
 *    scenario (a strictly decreasing array), all elements will be pushed onto 
 *    the stack and none will be popped, taking O(M) space. The Hash Map will 
 *    also take O(M) space in the best-case scenario.
 */