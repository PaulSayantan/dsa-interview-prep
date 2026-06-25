class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        prefix = 1
        suffix = 1
        n = len(nums)
        
        for i in range(n):
            # Reset to 1 if we encounter a zero
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1
            
            # Multiply from the front and the back simultaneously 
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
            
            # Update the max product
            max_prod = max(max_prod, prefix, suffix)
            
        return max_prod