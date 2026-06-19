from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Forward pass to compute left (prefix) products.
        # answer[i] will contain the product of all elements to the left of i.
        # Since there are no elements to the left of index 0, answer[0] remains 1.
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
            
        # Step 2: Backward pass to compute right (suffix) products on the fly.
        # right_product accumulates the product of all elements to the right of i.
        right_product = 1
        for i in range(n - 1, -1, -1):
            # Multiply the pre-calculated left product by the running right product.
            answer[i] *= right_product
            # Update the running right product for the next iteration (index i - 1).
            right_product *= nums[i]
            
        return answer