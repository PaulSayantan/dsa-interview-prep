from typing import List

class Solution:
    """
    Finds the majority element in a given list of numbers.
    
    The majority element is defined as the element that appears strictly more 
    than floor(n / 2) times. The problem guarantees that a majority element 
    always exists in the given array.

    Args:
        nums (List[int]): A list of integers representing the input array.

    Returns:
        int: The integer value of the majority element.

    Time Complexity: O(n), where n is the size of the array, as we iterate through it once.
    Space Complexity: O(1), as we only use two variables regardless of the input size.
    """
    def majorityElement(self, nums: List[int]) -> int:
        # ==============================================================================
        # ### Conceptual Breakdown
        # 
        # 1. Core Algorithmic Patterns:
        #    - Stream Processing / Counting
        #    - Boyer-Moore Majority Vote Algorithm (Optimal O(n) time, O(1) space)
        #
        # 2. Mental Intuition & Logic required:
        #    - Sub-optimal thoughts: Using a Hash Map to count frequencies takes O(n) 
        #      time but requires O(n) extra space. Sorting the array and picking the 
        #      middle element takes O(1) space but O(n log n) time.
        #    - The Optimal Intuition: Imagine the elements as factions fighting for dominance. 
        #      Since the majority element appears more than n/2 times, it has more "troops" 
        #      than all other factions combined.
        #    - If two different elements face off and cancel each other out (both are discarded),
        #      the majority element will inherently be the last one standing because it 
        #      strictly outnumbers the rest.
        #    - We maintain a `candidate` and a `count`. We iterate through the array:
        #      a. If `count` is 0, our current `candidate` has been fully cancelled out, 
        #         so we pick the current number as the new `candidate`.
        #      b. If the current number matches the `candidate`, we increment the `count` (+1).
        #      c. If it differs, we decrement the `count` (-1), signifying a cancellation.
        # ==============================================================================

        count = 0
        candidate = None

        for num in nums:
            # When the count drops to zero, we assign the current number as the new candidate
            if count == 0:
                candidate = num
            
            # If the current number is the candidate, it strengthens the count.
            # If it is a different number, they cancel each other out, weakening the count.
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

# ==========================================================================================
# ### Reusable Patterns & Key Takeaways
#
# - **Boyer-Moore Voting Algorithm**: This is a specialized, elegant pattern specifically 
#   designed for finding a strict majority element (> n/2 occurrences) in a sequence using 
#   constant O(1) space. It does not work for finding an element that is just the "most frequent" 
#   if it doesn't cross the > n/2 threshold.
#   
# - **The Cancellation Technique**: Whenever a problem requires finding a dominant presence 
#   against a mathematical threshold, consider if opposite elements can "cancel" each other out.
# - **Handling Space Constraints**: When an interviewer restricts a frequency/counting problem 
#   to O(1) space, Hash Maps are off the table. You must pivot to techniques like sorting 
#   (if time allows), Bit Manipulation, or mathematical state-tracking algorithms.
# ==========================================================================================