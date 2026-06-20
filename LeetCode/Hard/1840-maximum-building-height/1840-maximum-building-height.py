class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        """
        Calculates the maximum possible building height given city restrictions.
        """
        # STEP 1: Establish Boundaries
        # We append the known constraints for the first and last buildings to 
        # ensure our logic covers the entire span of the city uniformly.
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        # STEP 2: Sort the Data
        # Sorting by building ID ensures we evaluate the city from left to right.
        restrictions.sort()
        
        m = len(restrictions)
        
        # STEP 3: Forward Pass (Left-to-Right)
        # Cap the height of the current building based on how much it could 
        # possibly grow starting from the restricted height of the previous building.
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + dist)
            
        # STEP 4: Backward Pass (Right-to-Left)
        # Cap the height based on the next building's height + distance to ensure
        # steep drops required later in the array correctly constrain earlier buildings.
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + dist)
            
        max_height = 0
        
        # STEP 5: Calculate Peak Heights
        # Between any two globally valid restrictions, calculate the local maximum peak.
        for i in range(1, m):
            h1, h2 = restrictions[i - 1][1], restrictions[i][1]
            dist = restrictions[i][0] - restrictions[i - 1][0]
            
            # The highest peak formed by moving up from both sides
            peak = (h1 + h2 + dist) // 2
            max_height = max(max_height, peak)
            
        return max_height

"""
===============================================================================
FOOTNOTE: CODING & PROBLEM-SOLVING PATTERNS
===============================================================================

1. The "Two-Pass Constraint Propagation" Pattern
   - What it is: Iterating through an array once from left-to-right, and then 
     again from right-to-left, to satisfy constraints that "bleed" in both directions.
   - When to use it: When an element's valid state depends on its neighbors on 
     BOTH sides, but calculating both simultaneously is too complex. 
   - Other examples: LeetCode 135 (Candy), LeetCode 42 (Trapping Rain Water).

2. The "Dummy Boundary Normalization" Pattern
   - What it is: Manually injecting constraints for the absolute start and end of 
     your data range (e.g., adding [1, 0] and [n, n - 1]).
   - When to use it: When the edges of your dataset have implied rules but aren't 
     explicitly provided in the input. Doing this prevents you from writing messy 
     `if/else` edge cases to handle the start and end of the array.

3. The "Algebraic Peak / Intersection" Pattern
   - What it is: Translating physical rules (height changes by at most 1) into 
     geometric line equations (slopes of +1 and -1) to find an intersection.
   - When to use it: When finding a maximum/minimum limit between two constrained 
     points. Instead of looping step-by-step to find the middle peak (which would 
     cause a Time Limit Exceeded error), you use O(1) math: `(h1 + h2 + dist) // 2`.
===============================================================================
"""