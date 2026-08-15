# ============================================================================
# EDUCATIONAL GUIDE: RELATIVE SORT ARRAY
# ============================================================================

# ### Conceptual Breakdown
# 
# - **Core Algorithmic Pattern:** Hashing / Frequency Counting (Counting Sort variant).
# - **Alternative Pattern:** Custom Sorting with Hash Map lookups.
# 
# - **Mental Intuition & Logic:**
#   Your previous solution uses nested loops to physically swap elements in `arr1` 
#   based on matching elements in `arr2`. This results in an O(N * M) time complexity 
#   where N is the length of arr1 and M is the length of arr2. It works, but as you 
#   can see from the 299ms runtime, it creates a lot of overhead.
#
#   Instead of searching `arr1` repeatedly for every element in `arr2`, think of `arr2` 
#   as a "blueprint" or "recipe". 
#   
#   1. We need to know *exactly how many* of each ingredient (element) we have in `arr1`. 
#      A Hash Map (or frequency array) is the perfect data structure to count elements 
#      in O(N) time.
#   2. Once we have the counts, we can simply read our `arr2` blueprint. For every 
#      number in `arr2`, we check our frequency map, and append that number to our 
#      result list exactly as many times as it appeared in `arr1`.
#   3. After processing all elements in `arr2`, any elements left in our frequency 
#      map are the "leftovers" that didn't appear in `arr2`.
#   4. The problem asks us to sort these leftovers in ascending order and attach 
#      them to the end of our result.

import collections
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Sorts arr1 such that the relative ordering of items is the same as in arr2.
        Elements that do not appear in arr2 are placed at the end of arr1 in ascending order.

        Args:
            arr1 (List[int]): The array to be sorted.
            arr2 (List[int]): The reference array dictating the sort order. 
                              All elements in arr2 are distinct, and all elements in arr2 
                              are also in arr1.

        Returns:
            List[int]: A new array containing the sorted elements.

        Time Complexity: O(N * log(N)) in the worst case (if all elements are leftovers 
                         and need sorting), or O(N + M) if most elements are in arr2.
                         (N = len(arr1), M = len(arr2))
        Space Complexity: O(N) to store the frequency map and the resulting array.
        """
        
        # Step 1: Create a frequency map of all elements in arr1
        # collections.Counter does this in highly optimized O(N) time
        element_counts = collections.Counter(arr1)
        
        result = []
        
        # Step 2: Build the first part of the result using the arr2 blueprint
        for num in arr2:
            if num in element_counts:
                # Append the number 'freq' times to the result
                result.extend([num] * element_counts[num])
                
                # Delete the element from the map so only "leftovers" remain
                del element_counts[num]
        
        # Step 3: Collect all remaining elements (those not in arr2)
        leftovers = []
        for num, freq in element_counts.items():
            leftovers.extend([num] * freq)
            
        # Step 4: Sort the leftovers and append them to the final result
        # Note: sorting leftovers takes O(K * log K) where K is the number of leftovers
        result.extend(sorted(leftovers))
        
        return result


# ============================================================================
# ### Reusable Patterns & Key Takeaways
# ============================================================================
#
# 1. **Frequency Maps for Reordering:** 
#    Whenever a problem asks you to reorder, reconstruct, or group items based 
#    on a specific given sequence, counting the elements first (using a Hash Map 
#    or `collections.Counter`) is almost always faster than nested searching. 
#    It turns an O(N * M) search operation into an O(N) count + O(1) lookup.
#
# 2. **List Extension over Appending:**
#    In Python, `list.extend([x] * count)` is highly optimized at the C-level 
#    and is significantly faster and cleaner than writing a `for` loop to append 
#    the same item multiple times.
#
# 3. **Destructive Processing (Deleting from Hash Maps):**
#    Notice how we used `del element_counts[num]`. When processing data into categories 
#    (e.g., "in arr2" vs "not in arr2"), deleting keys as you process them is an 
#    elegant way to ensure the data structure only holds the "leftovers" at the end, 
#    saving you from having to do a second pass checking `if num not in arr2`.
# ============================================================================