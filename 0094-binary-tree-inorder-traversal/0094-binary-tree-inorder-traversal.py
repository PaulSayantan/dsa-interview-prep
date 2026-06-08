class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the inorder traversal of a binary tree's nodes' values.
        
        Intuition:
        To replicate the Left -> Root -> Right behavior without recursion, we need a 
        way to remember the nodes we've passed while digging down the left side of the 
        tree. A Stack (LIFO data structure) is perfect for this. We push nodes onto the 
        stack as we go left. When we can't go left anymore, we pop a node, process it, 
        and then move to its right child.

        Approach: Iterative DFS with Stack
        1. Use a pointer `curr` starting at the root.
        2. Loop as long as `curr` is not None OR the stack is not empty.
        3. Inner loop: Keep moving `curr` to `curr.left`, pushing each node to the stack.
        4. When `curr` is None, pop from the stack, record its value, and set `curr` to 
           the right child.
        
        Time Complexity: O(n) - Every node is pushed and popped from the stack exactly once.
        Space Complexity: O(n) - The stack can hold up to n nodes in the worst case 
                          (a skewed tree leaning completely left).
        """
        res = []
        stack = []
        curr = root
        
        while curr is not None or stack:
            # Go as far left as possible, pushing nodes onto the stack
            while curr is not None:
                stack.append(curr)
                curr = curr.left
                
            # We've hit a dead end on the left. Pop the last node.
            curr = stack.pop()
            
            # Process the node
            res.append(curr.val)
            
            # Move to the right subtree to continue traversal
            curr = curr.right
            
        return res