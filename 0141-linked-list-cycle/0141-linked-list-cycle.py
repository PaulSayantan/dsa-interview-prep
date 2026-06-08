# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        LeetCode 141. Linked List Cycle

        ------------------------------------------------------------
        INTUITION
        ------------------------------------------------------------

        We need to determine whether a linked list contains a cycle.

        A cycle exists if, while traversing the list, we eventually
        revisit a node that we have already seen before.

        Example:

            1 -> 2 -> 3 -> 4
                      ^    |
                      |____|

        In this example, node 4 points back to node 3, creating a loop.

        ------------------------------------------------------------
        NAIVE APPROACH (Using Hash Set)
        ------------------------------------------------------------

        We could store every visited node in a set.

        While traversing:
            - If current node already exists in the set,
              a cycle is present.
            - Otherwise add the node to the set and continue.

        Time Complexity : O(N)
        Space Complexity: O(N)

        ------------------------------------------------------------
        OPTIMAL APPROACH
        Floyd's Cycle Detection Algorithm
        (Tortoise and Hare Algorithm)
        ------------------------------------------------------------

        Use two pointers:

            slow -> moves 1 step at a time
            fast -> moves 2 steps at a time

        Case 1: No Cycle

            slow and fast eventually reach NULL.
            Traversal ends and we return False.

        Example:

            1 -> 2 -> 3 -> 4 -> NULL

            slow: 1 -> 2 -> 3 -> 4
            fast: 1 -> 3 -> NULL

        Case 2: Cycle Exists

            Since fast moves faster than slow,
            it will eventually catch up to slow
            inside the cycle.

        Example:

                 1 -> 2 -> 3
                      ^     |
                      |_____|

            Iteration 1:
                slow = 2
                fast = 3

            Iteration 2:
                slow = 3
                fast = 3

            slow == fast -> cycle detected

        ------------------------------------------------------------
        WHY DOES THIS WORK?
        ------------------------------------------------------------

        Once both pointers enter the cycle:

            Fast gains 1 node on slow every iteration
            because:

                fast moves 2 steps
                slow moves 1 step

            Relative speed = 1 node per iteration

        Therefore, fast must eventually catch slow,
        just like a faster runner eventually laps a
        slower runner on a circular track.

        ------------------------------------------------------------
        COMPLEXITY ANALYSIS
        ------------------------------------------------------------

        Time Complexity : O(N)
            Each pointer traverses at most O(N) nodes.

        Space Complexity : O(1)
            No extra data structures are used.

        ------------------------------------------------------------
        """

        # Both pointers start from the head.
        slow = fast = head

        # Continue while fast can move ahead safely.
        while slow is not None and fast is not None and fast.next is not None:

            # Slow pointer moves one step.
            slow = slow.next

            # Fast pointer moves two steps.
            fast = fast.next.next

            # If both pointers meet,
            # a cycle exists in the list.
            if slow == fast:
                return True

        # Fast reached the end of the list,
        # therefore no cycle exists.
        return False