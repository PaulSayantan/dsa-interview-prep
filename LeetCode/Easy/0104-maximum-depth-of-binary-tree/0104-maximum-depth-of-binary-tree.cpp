/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *
 *     TreeNode(int x, TreeNode *left, TreeNode *right)
 *         : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:

    /*
    --------------------------------------------------------------------
    INTUITION

    The maximum depth of the current node depends on the deeper of its
    two subtrees.

        depth(node)
            = 1 + max(depth(left), depth(right))

    Therefore, we first recursively solve the left and right subtrees
    and then compute the answer for the current node.

    This corresponds to Postorder Traversal.

    --------------------------------------------------------------------
    BASE CASE

    A nullptr node represents an empty tree whose depth is 0.

    --------------------------------------------------------------------
    TIME COMPLEXITY

    O(N)

    Every node is visited exactly once.

    --------------------------------------------------------------------
    SPACE COMPLEXITY

    O(H)

    H = height of the tree.
    --------------------------------------------------------------------
    */

    int maxDepth(TreeNode* root) {

        // Empty tree
        if (root == nullptr)
            return 0;

        // Compute left subtree depth
        int leftDepth = maxDepth(root->left);

        // Compute right subtree depth
        int rightDepth = maxDepth(root->right);

        // Current node contributes one level
        return 1 + std::max(leftDepth, rightDepth);
    }
};