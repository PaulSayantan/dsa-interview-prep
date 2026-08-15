"""
### Conceptual Breakdown
- Core Algorithmic Pattern: Divide and Conquer (specifically, Merge Sort).
- Mental Intuition & Logic:
  To sort an array efficiently with a strict O(n log n) time constraint, we can break 
  the problem down into smaller, trivial subproblems. An array consisting of a single 
  element is inherently already sorted. By recursively dividing the array in half until 
  we reach these single elements (the "Divide" step), we guarantee our tree depth is 
  O(log n). We then "conquer" the problem by merging these sorted halves back together. 
  The merging step utilizes a two-pointer approach to compare elements from two sorted 
  subarrays, picking the smaller element each time to efficiently build a larger sorted 
  segment in O(n) time.
"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array of integers in ascending order using Merge Sort.
        
        Args:
            nums (List[int]): The list of integers to be sorted.
            
        Returns:
            List[int]: The in-place sorted list of integers.
        """
        
        def merge_sort(left: int, right: int) -> None:
            """Recursively divides the array into halves until sorted."""
            # Base case: If the subarray has 1 or 0 elements, it is already sorted.
            if left >= right:
                return
            
            # Divide: Find the middle index to split the array.
            # Note: `left + (right - left) // 2` is used instead of `(left + right) // 2` 
            # to prevent potential integer overflow in other languages like Java or C++.
            mid = left + (right - left) // 2
            
            # Recursively sort the left and right halves.
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            
            # Conquer: Merge the two sorted halves back together.
            merge(left, mid, right)
            
        def merge(left: int, mid: int, right: int) -> None:
            """Merges two sorted subarrays back into the original array."""
            temp = []
            
            # Initialize pointers for the left subarray (i) and right subarray (j).
            i, j = left, mid + 1
            
            # Compare elements from both sorted halves.
            # Append the smaller element to the `temp` array to maintain sorted order.
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
                    
            # Clean Up: If there are remaining elements in the left subarray, 
            # they are already sorted and larger than merged elements. Append them.
            while i <= mid:
                temp.append(nums[i])
                i += 1
                
            # Clean Up: Similarly, append any remaining elements from the right subarray.
            while j <= right:
                temp.append(nums[j])
                j += 1
                
            # Overwrite the original array segment with the correctly sorted elements.
            for k in range(len(temp)):
                nums[left + k] = temp[k]

        # Trigger the sorting process on the full bounds of the array.
        merge_sort(0, len(nums) - 1)
        return nums

"""
### Reusable Patterns and Key Takeaways
1. Divide and Conquer Paradigm: 
   Whenever a problem asks you to process a large dataset with strict performance 
   constraints (like O(n log n) time), consider if the data can be split into smaller, 
   independent halves that are solved and then combined (e.g., Merge Sort, Quick Sort).

2. Two-Pointer Merging: 
   The logic used in the `merge` function is a highly reusable pattern for combining 
   two sorted entities. This exact two-pointer logic appears frequently in other 
   problems, such as "Merge Intervals", "Merge Sorted Arrays", and computing intersections.

3. Index-Based Recursion vs. Array Slicing: 
   Modifying the original array by passing pointer indices (`left`, `right`, `mid`) 
   rather than slicing new arrays in memory (e.g., `nums[left:mid]`) prevents massive 
   unnecessary memory allocation. This keeps the space complexity strictly bounded to 
   O(n) for the temporary merge array, avoiding Memory Limit Exceeded (MLE) errors.
"""