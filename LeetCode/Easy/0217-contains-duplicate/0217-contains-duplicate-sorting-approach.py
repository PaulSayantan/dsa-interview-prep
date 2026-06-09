from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        In-place Sorting Approach.
        
        Intuition:
        If an array contains duplicate elements, sorting the array will force 
        those duplicates to be adjacent to each other. By checking every element 
        with its immediate neighbor, we can easily catch duplicates.
        
        Complexity:
        - Time Complexity: O(N log N) due to the sorting step (`nums.sort()`).
        - Space Complexity: O(1) or O(N) depending on the language's sorting 
          implementation (Python's Timsort uses up to O(N) space in the worst case).
        """
        # Step 1: Sort the array to bring duplicates next to each other
        nums.sort()
        
        # Step 2: Iterate through the array and compare adjacent elements
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                return True  # Found a duplicate!
            i += 1
            
        return False  # All elements are unique