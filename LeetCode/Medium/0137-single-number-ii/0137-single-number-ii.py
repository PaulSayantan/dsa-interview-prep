class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(0, 32):
            summ = 0
            for num in nums:
                summ += (num >> i) & 1
            if summ % 3 == 1:
                result |= (1 << i)

        if result >= 2**31:
            return result - 2**32
        else:
            return result