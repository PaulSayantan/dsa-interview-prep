"""
### Conceptual Breakdown

- Core Algorithmic Pattern: Three-Pointer Approach / Partitioning (Dutch National Flag Algorithm).
- Mental Intuition & Logic: 
  The problem requires us to sort an array of three distinct values (0, 1, 2) in a single pass 
  with O(1) extra space. To achieve this, we can logically divide the array into four regions 
  using three pointers (`low`, `mid`, `high`):
  
  1. [0, low-1]     -> Region for 0s (Red)
  2. [low, mid-1]   -> Region for 1s (White)
  3. [mid, high]    -> Unexplored region (Unknowns)
  4. [high+1, n-1]  -> Region for 2s (Blue)
  
  The `mid` pointer acts as our active explorer. As it traverses the unexplored region:
  - If it sees a 0, we know it belongs at the beginning. We swap it with the `low` pointer 
    and advance both, expanding the 0s and 1s regions.
  - If it sees a 1, it's already in the correct relative middle region, so we just advance `mid`.
  - If it sees a 2, it belongs at the end. We swap it with the `high` pointer and shrink the 
    unexplored region by decrementing `high`. Crucially, we DO NOT advance `mid` here because 
    the swapped element coming from the `high` index is still unexplored and needs evaluating.
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts an array containing 0s, 1s, and 2s in-place.
        
        Args:
            nums (List[int]): The array of integers representing colors.
            
        Time Complexity: O(N) where N is the length of the array. The array is traversed 
                         exactly once by the `mid` pointer.
        Space Complexity: O(1) as the sorting is done purely in-place via swapping.
        """
        
        # 'low' tracks the rightmost boundary of the sorted 0s.
        # 'mid' is the active iterator traversing the array.
        # 'high' tracks the leftmost boundary of the sorted 2s.
        low = 0
        mid = 0
        high = len(nums) - 1
        
        # We iterate as long as the active pointer hasn't crossed the 'high' boundary.
        # Once mid > high, the entire array has been explored and partitioned.
        while mid <= high:
            
            # Case 1: We found a 0. It belongs on the left side of the array.
            if nums[mid] == 0:
                # Swap the current 0 to the 'low' boundary.
                nums[low], nums[mid] = nums[mid], nums[low]
                # Expand the 0s region by moving 'low' forward.
                low += 1
                # Move 'mid' forward because the element swapped from 'low' is guaranteed 
                # to be a 1 (or a 0 if low == mid), which doesn't need re-evaluating.
                mid += 1
                
            # Case 2: We found a 1. It belongs in the middle, which is right where it is.
            elif nums[mid] == 1:
                # Just expand the 1s region by moving our explorer forward.
                mid += 1
                
            # Case 3: We found a 2. It belongs on the right side of the array.
            else:
                # Swap the current 2 to the 'high' boundary.
                nums[mid], nums[high] = nums[high], nums[mid]
                # Expand the 2s region by moving 'high' backward.
                high -= 1
                # NOTE: We do NOT increment 'mid' here. The element we just swapped 
                # into the 'mid' position from 'high' could be a 0, 1, or 2. 
                # It must be evaluated on the next iteration.


"""
### Reusable Patterns & Key Takeaways

1. The Multi-Pointer Partitioning Pattern:
   This specific setup (low, mid, high) is extremely reusable for any problem requiring 
   you to segregate an array into three distinct buckets or categories (e.g., partitioning 
   elements less than, equal to, and greater than a pivot in QuickSort).

2. In-Place Swapping over Overwriting:
   When space constraints are O(1) and the data type is mutable, swapping allows you to 
   shift boundaries without losing data. 

3. Loop Termination & Pointer Desync Traps:
   A common bug is writing `while mid < high` instead of `<=`. The element at `high` is 
   part of the unexplored region and must be processed, so equality is required.
   Additionally, failing to use `if/elif/else` blocks (using sequential `if`s instead) 
   will cause the pointers to evaluate intermediate swapped states, breaking the logic.
"""