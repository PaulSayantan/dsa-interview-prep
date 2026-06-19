class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        
        // Step 1: Forward pass to compute left (prefix) products.
        // Initialize the first element to 1 as there are no elements to its left.
        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            // Each position stores the product of the previous position's 
            // prefix product and the previous element in the input array.
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        
        // Step 2: Backward pass to compute right (suffix) products on the fly.
        // rightProduct serves as an O(1) space accumulator.
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            // Combine the left product (stored in answer) with the right product.
            answer[i] *= rightProduct;
            // Accumulate the current element into the right product for the next step.
            rightProduct *= nums[i];
        }
        
        return answer;
    }
}