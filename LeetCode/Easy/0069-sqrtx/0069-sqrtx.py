"""
### Conceptual Breakdown

- Core Algorithmic Pattern: Binary Search (Search Space on Answers)
  Unlike traditional binary search that looks for an element in a given array, this pattern applies binary search to a range of potential numerical answers. 

- Mental Intuition:
  The mathematical square function is strictly monotonically increasing for non-negative numbers (e.g., if a < b, then a^2 < b^2). Finding the square root of a number `x` inherently maps to finding a specific target in a sorted sequence (from 0 up to `x`). 
  Since we want the integer square root (rounded down), we are looking for the largest integer `y` such that `y * y <= x`.

- Logic for Optimal Solution:
  1. Define the search space: The integer square root of a number `x` will always lie between `0` and `x`. We can optimize this slightly: for any `x >= 2`, its square root is always less than or equal to `x / 2`.
  2. Find the midpoint: Calculate `mid = low + (high - low) // 2`. This formula prevents potential integer overflow in languages with fixed-width integers (like Java or C++).
  3. Condition Check: 
     - If `mid * mid == x`, we've found the exact square root.
     - If `mid * mid < x`, `mid` is a valid candidate for the truncated square root. We record it as a potential answer and move our search to the right half (`low = mid + 1`) to see if there is a larger valid integer.
     - If `mid * mid > x`, `mid` is too large. We discard it and narrow our search to the left half (`high = mid - 1`).
  4. Termination: The loop ends when `low > high`. Our last recorded valid `mid` is the correct answer.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Calculates the square root of a non-negative integer x rounded down to the nearest integer.
        
        Args:
            x (int): The non-negative integer for which to find the square root.
            
        Returns:
            int: The truncated integer square root of x.
            
        Time Complexity: O(log x), as the search space is halved in each iteration.
        Space Complexity: O(1), no extra memory is allocated.
        """
        # Base cases for 0 and 1 to safely bypass the division by zero risk and optimize early.
        if x < 2:
            return x
            
        # The search space for the square root of x (for x >= 2) is bounded by 1 and x // 2.
        low, high = 1, x // 2
        root = 0
        
        while low <= high:
            # Calculate mid safely to avoid overflow in strictly typed languages.
            mid = low + (high - low) // 2
            
            # Optimization & Safety: 
            # Use division to check mid <= x // mid to prevent integer overflow 
            # during multiplication (equivalent to mid * mid <= x).
            if mid <= x // mid:
                # mid is a valid candidate. Save it and search for a potentially larger candidate.
                root = mid
                low = mid + 1
            else:
                # mid squared is greater than x. Narrow the search space to the left half.
                high = mid - 1
                
        return root

"""
### Reusable Patterns & Key Takeaways

1. Binary Search on Answer Space: 
   Binary search isn't solely for traversing pre-computed arrays. It is highly effective for finding an optimal value in a continuous or mathematically monotonic range (common in problems asking to "minimize the maximum" or find specific capacities).

2. Preventing Integer Overflow:
   - Midpoint Calculation: Get in the habit of using `low + (high - low) // 2` instead of `(low + high) // 2`.
   - Boundary Checks: Use `mid <= x // mid` instead of `mid * mid <= x`. While Python handles arbitrarily large integers automatically, this mathematical rearrangement is a critical safety practice in languages like C++, Java, and Go to prevent maximum integer limits from being breached during evaluation.

3. Monotonicity is the Cue: 
   Whenever a problem exhibits a boolean monotonic behavior—meaning if `y` is valid, all numbers `< y` are valid; and if `y` is invalid, all numbers `> y` are invalid—it is a prime candidate for a Binary Search optimization, dropping time complexity from O(N) to O(log N).
"""