# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both nodes are None. 
        # We've reached the end of both branches successfully.
        if not p and not q:
            return True
        
        # Base Case 2: Structural mismatch OR Value mismatch.
        # If only one is None, or if their values don't match, the trees are different.
        if not p or not q or p.val != q.val:
            return False
        
        # Recursive Step: Delegate to the children.
        # Both the left branches AND the right branches must be identical.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
