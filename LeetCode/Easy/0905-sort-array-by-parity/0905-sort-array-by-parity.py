class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def isOdd(k: int) -> bool:
            return k % 2 != 0
        i, j = 0, len(nums) - 1
        while i < j:
            if not isOdd(nums[i]):
                i += 1
            elif isOdd(nums[j]):
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums
            
            

        