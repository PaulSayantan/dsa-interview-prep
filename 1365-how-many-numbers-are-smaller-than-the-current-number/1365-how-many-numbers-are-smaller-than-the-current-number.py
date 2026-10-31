class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        temp = sorted(nums)
        small_map = dict()
        for i, n in enumerate(temp):
            if n not in small_map:
                small_map[n] = i

        result = []
        for i in range(len(nums)):
            result.append(small_map[nums[i]])

        return result

        