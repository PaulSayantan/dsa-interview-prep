/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /**
     * Calculates the inorder traversal of a binary tree iteratively.
     * * Intuition: Use a stack to simulate the recursive call stack. Push all left 
     * children, then pop, process, and move to the right child.
     * Approach: Iterative Depth-First Search with Stack.
     * Time Complexity: O(n)
     * Space Complexity: O(n) worst case for the explicitly managed stack.
     */
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        
        // Continue while there are unvisited nodes or nodes left in the stack
        while (curr != null || !stack.isEmpty()) {
            
            // Reach the left most Node of the current Node
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            
            // Current must be null at this point, pop from stack
            curr = stack.pop();
            
            // Add the popped node's value to the result
            res.add(curr.val);
            
            // Now, we visit the right subtree
            curr = curr.right;
        }
        
        return res;
    }
}