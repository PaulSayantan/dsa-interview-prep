class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # If duplicates are removed, the length will shrink
        return len(nums) != len(set(nums))