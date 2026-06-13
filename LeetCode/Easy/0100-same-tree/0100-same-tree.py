# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverseTree(node: Optional[TreeNode]):
            if node == None:
                yield None
                return
            yield node.val
            yield from traverseTree(node.left)
            yield from traverseTree(node.right)

        gen_p = traverseTree(p)
        gen_q = traverseTree(q)

        for val_p, val_q in itertools.zip_longest(gen_p, gen_q):
            if val_p != val_q:
                return False
        return True

        
        