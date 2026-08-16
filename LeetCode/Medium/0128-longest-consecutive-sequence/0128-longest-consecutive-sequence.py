class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_streak = 0

        for num in numset:
            # Check if this is the start of a sequence
            if (num - 1) not in numset:
                current_num = num
                current_streak = 1

                # Count upwards as far as the sequence goes
                while (current_num + 1) in numset:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak