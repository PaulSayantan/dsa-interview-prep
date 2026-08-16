"""
Problem: Longest Consecutive Sequence

### Conceptual Breakdown
- Core Algorithmic Pattern: Hashing (Set), Intelligent Sequence Verification.
- Mental Intuition and Logic:
  The naive approach to finding consecutive elements is to sort the array, which requires 
  O(n log n) time. To achieve an optimal O(n) time complexity, we must leverage the O(1) 
  average time complexity for lookups provided by a Hash Set. 
  
  The fundamental logical leap is realizing that a number is only the *true start* of a 
  new consecutive sequence if the number immediately preceding it (num - 1) does not 
  exist in the array. 
  
  By first converting the array to a set, we can iterate through the elements and apply 
  this boundary check. We strictly limit our upward counting (num + 1, num + 2, ...) to 
  only those numbers that are confirmed sequence starters. This prevents redundant 
  backward/forward counting and ensures each number in the array is visited at most 
  twice (once in the outer loop, and at most once in the inner while loop), guaranteeing 
  strict O(n) execution time.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in an unsorted array.
        
        Args:
            nums (List[int]): An unsorted list of integers.
            
        Returns:
            int: The length of the longest consecutive sequence.
            
        Time Complexity: O(n) - We iterate through the array to build the set, and then 
                         iterate through the set. The inner while loop only executes for 
                         sequence starters, meaning we process each number at most O(1) 
                         times within the loop.
        Space Complexity: O(n) - A Hash Set is created to store the unique numbers.
        """
        # Convert list to a set to remove duplicates and enable O(1) lookups
        numset = set(nums)
        longest_streak = 0

        for num in numset:
            # OPTIMIZATION LOCK: Only initiate a sequence check if 'num' is the lowest value
            # of a potential sequence. If 'num - 1' is in the set, 'num' is simply a middle 
            # or end piece of a sequence we have either already counted or will count later.
            if (num - 1) not in numset:
                current_num = num
                current_streak = 1

                # Count upwards as far as the sequence goes.
                # Because of our boundary check above, this while loop only fully executes
                # exactly once for each distinctly connected sequence block.
                while (current_num + 1) in numset:
                    current_num += 1
                    current_streak += 1

                # Update the maximum streak found across all evaluated sequences
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

"""
### Reusable Patterns and Key Takeaways

1. The "Left-Boundary" Check: 
   Whenever dealing with continuous ranges, intervals, or sequences in an unsorted dataset, 
   checking for a boundary condition (e.g., checking if `value - 1` exists) is a powerful 
   mechanism. It allows you to identify the "root" of a group, eliminating redundant work 
   and flattening time complexity from O(n^2) to O(n).

2. Space-Time Tradeoffs:
   Trading O(1) space for O(n) space by introducing a Hash Set is the industry-standard 
   technique for bypassing O(n log n) sorting requirements in favor of linear O(n) scans.

3. Set vs. Dictionary (Hash Map) Selection:
   If the algorithm only requires existence verification rather than mapping a key to a 
   persisted state (like in a dynamic programming approach), always prefer a Hash Set. 
   It eliminates the memory overhead of tracking key-value pairs and keeps the logic 
   streamlined.
"""