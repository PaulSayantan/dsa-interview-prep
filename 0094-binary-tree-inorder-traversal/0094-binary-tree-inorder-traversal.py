# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the inorder traversal of a binary tree's nodes' values.
        
        Intuition:
        Inorder traversal dictates that we must visit the nodes in a specific sequence:
        1. Explore the entire left subtree.
        2. Visit the current node (the "root" of the current subtree).
        3. Explore the entire right subtree.
        This naturally maps to a recursive function.

        Approach: Recursive DFS
        We define a helper function `traversal(node)` that visits the left child, 
        appends the current node's value to a shared results list, and then visits 
        the right child. The base case is hitting a `None` node (a leaf's child), 
        at which point we just return.
        
        Time Complexity: O(n) - We visit every node in the tree exactly once.
        Space Complexity: O(n) - In the worst case (a completely skewed/unbalanced tree), 
                          the recursion stack will grow to the size of n. In a perfectly 
                          balanced tree, space is O(log n).
        """
        res = []
        
        def traversal(node):
            # Base Case: If the node doesn't exist, stop traversing this branch.
            if node == None: 
                return
            
            # Step 1: Traverse the left subtree
            traversal(node.left)
            
            # Step 2: Process the current node
            res.append(node.val)
            
            # Step 3: Traverse the right subtree
            traversal(node.right)
        
        # Start the recursive traversal from the root node
        traversal(root)
        
        return res