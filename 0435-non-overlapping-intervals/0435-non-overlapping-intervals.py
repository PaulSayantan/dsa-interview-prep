class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        ordered_intervals = sorted(intervals, key=lambda interval: interval[1])
        count = 0
        prev_end = float("-inf")
        for (start, end) in ordered_intervals:
            if start >= prev_end:
                count += 1
                prev_end = end

        return len(intervals) - count
        