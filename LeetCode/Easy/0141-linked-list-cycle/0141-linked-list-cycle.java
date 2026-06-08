/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {

    /**
     * LeetCode 141. Linked List Cycle
     *
     * ============================================================
     * INTUITION
     * ============================================================
     *
     * We need to determine whether a linked list contains a cycle.
     *
     * A cycle exists if some node's next pointer eventually points
     * back to a previously visited node.
     *
     * Example:
     *
     *      1 -> 2 -> 3 -> 4
     *                ^    |
     *                |____|
     *
     * If we keep traversing, we will never reach null.
     *
     * ============================================================
     * OPTIMAL APPROACH
     * Floyd's Cycle Detection Algorithm
     * (Tortoise and Hare)
     * ============================================================
     *
     * Maintain two pointers:
     *
     *      slow -> moves 1 step at a time
     *      fast -> moves 2 steps at a time
     *
     * If there is no cycle:
     *      fast reaches null.
     *
     * If a cycle exists:
     *      fast eventually catches slow.
     *
     * Example:
     *
     *      1 -> 2 -> 3
     *           ^     |
     *           |_____|
     *
     * Iteration 1:
     *      slow = 2
     *      fast = 3
     *
     * Iteration 2:
     *      slow = 3
     *      fast = 3
     *
     * slow == fast
     * => cycle detected
     *
     * ============================================================
     * WHY DOES THIS WORK?
     * ============================================================
     *
     * Once both pointers enter the cycle:
     *
     *      slow moves 1 node per iteration
     *      fast moves 2 nodes per iteration
     *
     * Relative speed = 1 node per iteration.
     *
     * Therefore, fast continuously gains on slow and
     * must eventually meet it within the cycle.
     *
     * Similar to a faster runner eventually lapping
     * a slower runner on a circular track.
     *
     * ============================================================
     * COMPLEXITY ANALYSIS
     * ============================================================
     *
     * Time Complexity  : O(N)
     * Space Complexity : O(1)
     *
     * ============================================================
     */
    public boolean hasCycle(ListNode head) {

        // Initialize both pointers at the head.
        ListNode slow = head;
        ListNode fast = head;

        // Continue while fast can safely move two steps.
        while (slow != null && fast != null && fast.next != null) {

            // Move slow pointer by one step.
            slow = slow.next;

            // Move fast pointer by two steps.
            fast = fast.next.next;

            // If both pointers meet,
            // a cycle exists.
            if (slow == fast) {
                return true;
            }
        }

        // Fast pointer reached the end,
        // therefore no cycle exists.
        return false;
    }
}