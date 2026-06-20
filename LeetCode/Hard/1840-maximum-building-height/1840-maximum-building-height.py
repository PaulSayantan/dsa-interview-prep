class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Step 1: Add boundary constraints
        # Building 1 must have height 0, and building n can be at most n - 1
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        # Step 2: Sort the restrictions by building ID
        restrictions.sort()
        
        m = len(restrictions)
        
        # Step 3: Forward Pass (Left to Right)
        # Cap the height of the current building based on the previous building's height + distance
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + dist)
            
        # Step 4: Backward Pass (Right to Left)
        # Cap the height of the current building based on the next building's height + distance
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + dist)
            
        max_height = 0
        
        # Step 5: Calculate Peak Heights
        # Between any two valid restrictions, calculate the local maximum peak
        for i in range(1, m):
            h1, h2 = restrictions[i - 1][1], restrictions[i][1]
            dist = restrictions[i][0] - restrictions[i - 1][0]
            
            # The highest peak formed by moving up from both sides
            peak = (h1 + h2 + dist) // 2
            max_height = max(max_height, peak)
            
        return max_height