class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem:
        Reverse a singly linked list.

        ---------------------------------------------------------------
        RECURSIVE INTUITION
        ---------------------------------------------------------------

        Instead of reversing the links while moving forward, we first
        travel all the way to the end of the list.

        Example:

            1 -> 2 -> 3 -> 4 -> 5

        We recursively move toward node 5.

        Once we reach node 5, we know that:

            5

        is already a reversed list (a single node is trivially reversed).

        Then while returning from recursion, each node asks:

            "The sublist after me has already been reversed.
             How do I attach myself at the end of that reversed part?"

        ---------------------------------------------------------------
        RECURSION TREE
        ---------------------------------------------------------------

        reverse(1)
            reverse(2)
                reverse(3)
                    reverse(4)
                        reverse(5)

        Node 5 reaches the base case and becomes the new head.

        While unwinding:

            5 <- 4
            5 <- 4 <- 3
            5 <- 4 <- 3 <- 2
            5 <- 4 <- 3 <- 2 <- 1

        ---------------------------------------------------------------
        KEY OBSERVATION
        ---------------------------------------------------------------

        Suppose we are currently at node 3:

            head = 3

        and the recursive call has already reversed everything after it:

            5 -> 4

        while node 3 still looks like:

            3 -> 4

        Therefore:

            head.next        = node 4
            head.next.next   = node 4's next

        Setting

            head.next.next = head

        means:

            4 -> 3

        which connects node 3 to the end of the reversed sublist.

        After that, we must disconnect the old forward pointer:

            head.next = None

        otherwise we'd create:

            3 <-> 4

        causing a cycle.

        ---------------------------------------------------------------
        TIME COMPLEXITY
        ---------------------------------------------------------------
        O(n)
        Each node is visited exactly once.

        ---------------------------------------------------------------
        SPACE COMPLEXITY
        ---------------------------------------------------------------
        O(n)
        Because recursion uses the call stack.
        """

        # Base Case:
        #
        # If the list is empty, or contains only one node,
        # it is already reversed, so simply return it.
        #
        # Examples:
        #
        #   None           -> None
        #   5              -> 5
        #
        if head is None or head.next is None:
            return head

        # -----------------------------------------------------------
        # Recursive Step
        #
        # Reverse everything after the current node.
        #
        # Example:
        #
        # Current list:
        #   1 -> 2 -> 3 -> 4 -> 5
        #
        # At node 1, this call:
        #
        #   reverseList(2)
        #
        # eventually returns:
        #
        #   5 -> 4 -> 3 -> 2
        #
        # and 'new_head' points to node 5.
        # -----------------------------------------------------------
        new_head = self.reverseList(head.next)

        # -----------------------------------------------------------
        # Reversal Step
        #
        # Before:
        #
        #   head      head.next
        #     3 -----> 4
        #
        # and the deeper recursion has already reversed:
        #
        #   5 -> 4
        #
        # We now make node 4 point back to node 3:
        #
        #   5 -> 4 -> 3
        #
        # by doing:
        # -----------------------------------------------------------
        head.next.next = head

        # -----------------------------------------------------------
        # Disconnect Step
        #
        # Originally node 3 still points to node 4:
        #
        #   3 -> 4
        #
        # If we don't remove this connection, we'll have:
        #
        #   3 <-> 4
        #
        # which forms a cycle.
        #
        # Therefore we set:
        # -----------------------------------------------------------
        head.next = None

        # -----------------------------------------------------------
        # new_head always points to the original tail node.
        #
        # For:
        #
        #   1 -> 2 -> 3 -> 4 -> 5
        #
        # new_head is node 5.
        #
        # Every recursive call returns this same node upward until
        # the very first call receives and returns it.
        # -----------------------------------------------------------
        return new_head