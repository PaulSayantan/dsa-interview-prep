class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        numset = set(nums)

        memo = {}
        for num in numset:
            k = num - 1
            length = 1
            if k in memo:
                memo[num] = memo[k] + 1
                length = memo[k] + 1
            else:
                while k in numset:
                    length += 1
                    k -= 1
                memo[num] = length
            maxlen = max(maxlen, length)

        return maxlen

        