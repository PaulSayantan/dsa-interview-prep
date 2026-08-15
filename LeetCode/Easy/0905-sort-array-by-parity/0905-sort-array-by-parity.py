"""
Problem: Sort Array By Parity (LeetCode 905)

### Conceptual Breakdown

- Core Algorithmic Patterns: 
  1. Two Pointers (Opposite Direction)
  2. In-place Array Partitioning (Hoare's Partition scheme variation)

- Mental Intuition and Logic:
  The objective is to segregate an array into two continuous zones based on a binary 
  condition (even vs. odd). Rather than allocating a new array and taking up O(N) 
  extra space, we can achieve an optimal O(1) space complexity by manipulating the 
  array in place.
  
  Imagine two boundaries shrinking inward. The `left` pointer defines the edge of the 
  "even numbers" territory, and the `right` pointer defines the edge of the "odd 
  numbers" territory. 
  
  As we scan inward:
  - If `nums[left]` is even, it rightfully belongs in the left territory. We simply 
    advance the `left` pointer.
  - If `nums[right]` is odd, it rightfully belongs in the right territory. We simply 
    decrement the `right` pointer.
  - The bottleneck (the `else` case) only occurs when BOTH pointers are pointing to 
    elements that belong in the other's territory (left is odd, right is even). 
    A single swap fixes both elements' placements simultaneously. 
  
  This approach guarantees that every element is evaluated at most once, locking in 
  a strict O(N) time complexity, which is optimal for array traversal and exactly 
  what interviewers look for in foundational array manipulation questions.
"""

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Sorts an array by parity, placing all even integers at the beginning 
        followed by all odd integers.
        
        Args:
            nums (List[int]): The input array of integers to be partitioned.
            
        Returns:
            List[int]: The in-place modified array satisfying the parity condition.
            
        Complexity:
            Time: O(N) - Single pass through the array.
            Space: O(1) - In-place swaps, no auxiliary data structures.
        """
        # Initialize two pointers at the absolute boundaries of the array
        left, right = 0, len(nums) - 1
        
        # Traverse until the two boundaries meet or cross
        while left < right:
            # Condition 1: Left element is already even.
            # Use bitwise AND for a micro-optimization over modulo operator.
            # (num & 1) == 0 means the least significant bit is 0 (number is even).
            if (nums[left] & 1) == 0:
                left += 1
                
            # Condition 2: Right element is already odd.
            # (num & 1) == 1 means the least significant bit is 1 (number is odd).
            elif (nums[right] & 1) == 1:
                right -= 1
                
            # Condition 3: Left is odd AND Right is even.
            # Both are displaced. Swap them to correct their positions.
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        return nums

"""
### Reusable Patterns & Key Takeaways

1. Two-Pointer Partitioning: 
   This is a fundamental building block often used as a subroutine in more complex 
   system design or algorithmic problems (like the partition step in Quicksort). 
   Whenever a problem asks to group or separate items based on a true/false condition 
   (e.g., positive/negative, zeroes/non-zeroes, true/false), an opposite-direction 
   two-pointer approach is usually the most optimal in-place solution.

2. Bitwise Operations for Parity: 
   Using `num & 1` instead of `num % 2 != 0` is a highly regarded micro-optimization in 
   compiled languages and demonstrates a deeper understanding of CPU-level operations. 
   While Python handles modulo efficiently, bitwise checks show mechanical sympathy.

3. State Management:
   Notice how the `if-elif-else` structure prevents unnecessary redundant checks. 
   By prioritizing the "happy paths" (where the pointers just move), we minimize the 
   amount of active memory writing (swaps) to only when absolutely mathematically required.
"""