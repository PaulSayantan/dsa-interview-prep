#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(const std::vector<int>& nums) {
        int n = nums.size();
        // Initialize the answer vector with 1s to handle the boundaries implicitly.
        std::vector<int> answer(n, 1);
        
        // Step 1: Forward pass to compute left (prefix) products.
        // We start at index 1 and use the previously stored product.
        for (int i = 1; i < n; ++i) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        
        // Step 2: Backward pass to compute right (suffix) products on the fly.
        // right_product is the scalar variable enabling the O(1) space constraint.
        int right_product = 1;
        for (int i = n - 1; i >= 0; --i) {
            // The final result for index i is left_product * right_product.
            answer[i] *= right_product;
            // Update the suffix accumulator.
            right_product *= nums[i];
        }
        
        return answer;
    }
};