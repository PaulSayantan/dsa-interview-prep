import java.util.HashMap;
import java.util.Map;

class Solution {

    /**
     * Problem:
     *     Given an array of integers and a target value, return the indices
     *     of the two numbers such that they add up to the target.
     *
     * Approach: Hash Map (One-Pass)
     *
     * Intuition:
     *     For every number nums[i], we need another number:
     *
     *         complement = target - nums[i]
     *
     *     If this complement has already been seen earlier in the array,
     *     then we have found the required pair.
     *
     *     To efficiently determine whether the complement exists,
     *     we store previously visited numbers in a HashMap:
     *
     *         value -> index
     *
     *     HashMap provides O(1) average lookup time, allowing us to solve
     *     the problem in a single pass.
     *
     * Algorithm:
     *     1. Create an empty HashMap.
     *     2. Traverse the array from left to right.
     *     3. For each element:
     *          - Calculate its complement.
     *          - Check if the complement already exists in the map.
     *          - If it exists, return the stored index and current index.
     *          - Otherwise, store the current number and its index.
     *     4. If no valid pair is found, return an empty array.
     *
     * Example:
     *     nums   = [2, 7, 11, 15]
     *     target = 9
     *
     *     i = 0, num = 2
     *     complement = 7
     *     map = {2 -> 0}
     *
     *     i = 1, num = 7
     *     complement = 2
     *     2 exists in map
     *
     *     Return [0, 1]
     *
     * Time Complexity:
     *     O(n)
     *     Each element is processed exactly once.
     *
     * Space Complexity:
     *     O(n)
     *     In the worst case, all elements are stored in the HashMap.
     */
    public int[] twoSum(int[] nums, int target) {

        // Stores:
        // number -> index
        Map<Integer, Integer> map = new HashMap<>();

        // Traverse the array once
        for (int i = 0; i < nums.length; i++) {

            // Number required to reach the target
            int complement = target - nums[i];

            // If complement was seen before,
            // we have found the answer
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }

            // Otherwise store the current number
            // for future complement lookups
            map.put(nums[i], i);
        }

        // No valid pair found
        return new int[0];
    }
}