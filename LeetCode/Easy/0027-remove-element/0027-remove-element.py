"""
### Conceptual Breakdown

* Core Algorithmic Pattern: Two Pointers (Reader/Writer Pointers)
* Mental Intuition & Logic: 
  The problem asks us to modify the array in-place, removing specific elements without 
  allocating extra space for a new array. To do this, we can think of the array as having 
  two parts: a "valid" section at the beginning and an "unexplored/invalid" section. 
  
  We can use two pointers starting at index 0:
  1. A 'reader' pointer (often just the loop index 'i') that scans through every element.
  2. A 'writer' pointer that keeps track of the position where the next valid element 
     should be placed.

  As the 'reader' scans the array, if it finds an element that is NOT the target value, 
  it means this is a valid element we want to keep. We write this element to the 'writer' 
  position and increment the 'writer' pointer. If the element IS the target value, we 
  simply skip it. By the end of the scan, the 'writer' pointer will inherently represent 
  the total count of valid elements, which is the exact number 'k' we need to return.
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of a specified value in an array in-place.
        
        Args:
            nums (List[int]): The input array of integers.
            val (int): The integer value to be removed from the array.
            
        Returns:
            int: The number of elements (k) in nums that are not equal to `val`.
        """
        
        # 'writer' points to the index where the next valid element will be placed.
        # It also acts as the counter for how many valid elements we have found.
        writer = 0
        
        # 'reader' iterates through the entire array to evaluate each element.
        for reader in range(len(nums)):
            
            # Learning Note: We only take action if the current element is valid 
            # (i.e., it does not match the value we are trying to remove).
            if nums[reader] != val:
                
                # Overwrite the element at the 'writer' index with the valid element.
                # If reader == writer, it safely overwrites itself with no issue.
                nums[writer] = nums[reader]
                
                # Advance the 'writer' pointer to prepare for the next valid element.
                writer += 1
                
        # The 'writer' index now correctly represents the length of the modified array.
        return writer

"""
### Reusable Patterns & Key Takeaways

1. In-Place Array Modification: Whenever a problem requires you to modify an array 
   in-place (O(1) extra space) by removing, filtering, or compacting elements, the 
   Reader/Writer Two-Pointer technique is almost always the optimal approach.
   
2. Dedicated Pointer Roles: Clearly defining the responsibility of each pointer 
   simplifies the logic significantly:
   - The Reader: Explores the data and checks conditions.
   - The Writer: Builds and maintains the valid output state.

3. Overwriting vs. Deleting: Arrays are contiguous blocks of memory. Actually 
   "deleting" an element from the middle of an array is an O(N) operation because it 
   requires shifting all subsequent elements down. By overwriting the "garbage" values 
   with valid ones in a single pass, we achieve an optimal O(N) time complexity.
"""