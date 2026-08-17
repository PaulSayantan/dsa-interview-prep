class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True

        i = 0
        while i < len(nums) - 2 and nums[i] == nums[i+1]:
            i += 1

        if nums[i] < nums[i + 1]:
            dir = False
        else:
            dir = True
        i += 1
        
        for j in range(i, len(nums) - 1):
            if dir and nums[j] < nums[j+1]:
                return False
            elif not dir and nums[j] > nums[j+1]:
                return False

        return True
        
