from typing import List

class Solution:
    """
    Solves the 'Container With Most Water' problem using a Two-Pointer approach.
    """

    def maxArea(self, height: List[int]) -> int:
        """
        Calculates the maximum amount of water a container can store.

        Args:
            height (List[int]): An array of integers where each element represents 
                                the height of a vertical line.

        Returns:
            int: The maximum area of water that can be contained.

        Time Complexity:
            O(n) - The array is traversed at most once as the pointers converge.
            
        Space Complexity:
            O(1) - Only a few integer variables are allocated, requiring constant space.
        """
        # Initialize pointers at the extremes to maximize the initial width
        left = 0
        right = len(height) - 1
        
        max_area = 0
        
        # Traverse until the two pointers meet
        while left < right:
            # The height of the water is limited by the shorter line
            current_height = min(height[left], height[right])
            width = right - left
            
            # Calculate current area and update max_area if necessary
            current_area = width * current_height
            if current_area > max_area:
                max_area = current_area
            
            # Greedily move the pointer pointing to the shorter line inward.
            # Rationale: Moving the taller line inward cannot possibly increase the area 
            # because the new area would still be bottlenecked by the current shorter line, 
            # while the width strictly decreases.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

    """
    ===========================================================================
    FOOTNOTE: LEARNING NOTES & REUSABLE PATTERNS
    ===========================================================================
    1. THE CONVERGING POINTERS PATTERN
       - Definition: Initializing pointers at the start (0) and end (n-1) of 
         an array and moving them towards the center based on a condition.
       - When to use: Commonly applied when dealing with pairs in a sequence, 
         especially when you need to evaluate maximums/minimums of combinations 
         (like area/width constraints) or when searching for target sums in 
         sorted arrays (e.g., Two Sum II).
         
    2. SEARCH SPACE REDUCTION
       - The naive approach (checking every pair) requires O(n^2) time.
       - The Two-Pointer strategy systematically eliminates O(n) pairs in a 
         single step. By dropping the shorter line, you mathematically prove 
         that the shorter line paired with ANY of the remaining inner lines 
         will yield a smaller area than it did with the current outer line.
         
    3. BOTTLENECK OPTIMIZATION 
       - When an equation utilizes a `min()` or `max()` bound constraint 
         (Area = width * min(h1, h2)), identify the "bottleneck" (the min value). 
       - To optimize the overall calculation across iterations, always shed 
         the bottleneck variable.
    ===========================================================================
    """