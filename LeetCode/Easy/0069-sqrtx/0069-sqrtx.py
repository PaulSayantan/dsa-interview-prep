class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        root = 0
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
                root = mid
            else:
                return mid
                

        return root
            