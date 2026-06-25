class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = float('-inf')
        
        # perform forward pass and calculate prefix product
        prefixProd = 1
        for n in nums:
            prefixProd *= n
            maxProd = max(maxProd, prefixProd)
            if prefixProd == 0:
                prefixProd = 1

        # perform backward pass and calculate the suffix product
        suffixProd = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixProd *= nums[i]
            maxProd = max(maxProd, suffixProd)
            if suffixProd == 0:
                suffixProd = 1

        return maxProd
