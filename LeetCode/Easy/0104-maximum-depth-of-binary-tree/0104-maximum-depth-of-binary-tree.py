# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the maximum depth (height) of a binary tree.

        --------------------------------------------------------------------
        INTUITION
        --------------------------------------------------------------------
        Think of the problem from the perspective of a single node.

        For any node:
            - Its left subtree already knows its maximum depth.
            - Its right subtree already knows its maximum depth.

        Therefore, the depth of the current node becomes:

                1 + max(left subtree depth, right subtree depth)

        The '+1' accounts for the current node itself.

        --------------------------------------------------------------------
        RECURSIVE THOUGHT PROCESS
        --------------------------------------------------------------------

                      3
                    /   \
                   9     20
                        /  \
                      15    7

        Starting from node 3:

        depth(3)
            = 1 + max(depth(9), depth(20))

        depth(9)
            = 1 + max(depth(None), depth(None))
            = 1

        depth(20)
            = 1 + max(depth(15), depth(7))

        depth(15)
            = 1

        depth(7)
            = 1

        Therefore:

        depth(20) = 2
        depth(3)  = 3

        --------------------------------------------------------------------
        WHY POSTORDER TRAVERSAL?
        --------------------------------------------------------------------
        We cannot compute the answer for the current node until both children
        have already computed their depths.

        Thus, the order is:

            Left subtree
            Right subtree
            Current node

        which is Postorder traversal.

        --------------------------------------------------------------------
        BASE CASE
        --------------------------------------------------------------------
        If the node is None, there is no tree and its depth is 0.

        --------------------------------------------------------------------
        TIME COMPLEXITY
        --------------------------------------------------------------------
        O(N)
        Every node is visited exactly once.

        --------------------------------------------------------------------
        SPACE COMPLEXITY
        --------------------------------------------------------------------
        O(H)

        H = height of tree

        Best case (balanced tree): O(log N)
        Worst case (skewed tree):  O(N)
        """

        # Empty tree has depth 0.
        if root is None:
            return 0

        # Recursively find depth of left subtree.
        leftDepth = self.maxDepth(root.left)

        # Recursively find depth of right subtree.
        rightDepth = self.maxDepth(root.right)

        # Current node contributes 1 level to the larger subtree depth.
        return 1 + max(leftDepth, rightDepth)