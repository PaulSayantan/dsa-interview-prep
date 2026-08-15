# ============================================================================
# EDUCATIONAL GUIDE: RELATIVE SORT ARRAY (OPTIMIZED)
# ============================================================================

# ### Conceptual Breakdown
# 
# - **Core Algorithmic Pattern:** True Counting Sort (Array-based frequency map).
# 
# - **Mental Intuition & Logic:**
#   Your previous solution was great, but Hash Maps have a slight overhead, and 
#   we still had to use `sorted(leftovers)` which takes O(K log K) time. 
#
#   Since we know the problem constraints say elements are between 0 and 1000, 
#   we can use a simple list of size 1001 as our "frequency map". 
#   
#   1. We count the occurrences of each number in `arr1` using an array where the 
#      index represents the number, and the value represents its frequency.
#   2. We build the first part of our result using the `arr2` blueprint, just 
#      like before, and zero out the counts as we use them.
#   3. For the leftovers, instead of gathering them and sorting them, we simply 
#      iterate through our counting array from index 0 up to 1000. Because we are 
#      iterating through indices in ascending order, any remaining counts are 
#      naturally appended in strictly ascending sorted order! No `sort()` needed!

from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Sorts arr1 based on the relative ordering of items in arr2.
        Elements not in arr2 are placed at the end in ascending order.
        
        This optimized version uses an array for counting to achieve linear time.

        Args:
            arr1 (List[int]): The array to be sorted. Elements are between 0 and 1000.
            arr2 (List[int]): The reference array dictating the sort order. 

        Returns:
            List[int]: A new array containing the sorted elements.

        Time Complexity: O(N + M + U), where N is len(arr1), M is len(arr2), 
                         and U is the maximum possible value in arr1 (1000). 
                         This is strictly linear O(N) and eliminates the O(N log N) sort.
        Space Complexity: O(U) for the frequency array. Since U is a constant 1000, 
                          this effectively boils down to O(1) auxiliary space!
        """
        
        # Step 1: Create a fixed-size counting array (size 1001 for elements 0-1000)
        max_val = 1001 
        count = [0] * max_val
        
        # Step 2: Populate the frequency array
        for num in arr1:
            count[num] += 1
            
        result = []
        
        # Step 3: Build the result according to the arr2 blueprint
        for num in arr2:
            # Append 'num' exactly count[num] times
            result.extend([num] * count[num])
            # Zero out the count so we know it has been processed
            count[num] = 0
            
        # Step 4: Append the leftovers naturally sorted
        # By iterating from 0 to 1000, we automatically get ascending order
        for num in range(max_val):
            if count[num] > 0:
                result.extend([num] * count[num])
                
        return result


# ============================================================================
# ### Reusable Patterns & Key Takeaways
# ============================================================================
#
# 1. **Fixed-Size Counting Sort:** 
#    Whenever a problem involves sorting, grouping, or hashing numbers, ALWAYS 
#    check the constraints. If the maximum value (U) is small (e.g., U <= 10^4), 
#    an array-based counting sort `counts = [0] * (U + 1)` is significantly faster 
#    and uses less memory overhead than a Hash Map.
#
# 2. **"Free" Sorting:**
#    The biggest advantage of a counting array is that its indices are inherently 
#    sorted. Iterating through the array automatically yields the elements in 
#    ascending order, completely bypassing the O(N log N) barrier of comparison-based 
#    sorting algorithms.
# ============================================================================