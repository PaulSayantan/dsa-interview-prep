# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        ITERATIVE BFS SOLUTION

        ----------------------------------------------------------------
        INTUITION

        Each layer of the tree contributes exactly one level to the
        overall depth.

        Therefore, if we perform a level-order traversal (BFS), we can
        simply count how many levels are present.

        ----------------------------------------------------------------
        ALGORITHM

        1. Put the root into a queue.
        2. Process one complete level at a time.
        3. After finishing a level, increase depth by 1.
        4. Continue until the queue becomes empty.

        ----------------------------------------------------------------
        TIME COMPLEXITY

        O(N)

        ----------------------------------------------------------------
        SPACE COMPLEXITY

        O(W)

        W = maximum width of the tree.
        """

        if root is None:
            return 0

        queue = deque([root])

        depth = 0

        while queue:

            # Number of nodes currently belonging to this level.
            level_size = len(queue)

            # Process the entire level.
            for _ in range(level_size):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # One level has been completely processed.
            depth += 1

        return depth