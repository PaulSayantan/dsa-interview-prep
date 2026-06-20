from typing import List

class Solution:
    """
    Problem: LeetCode 200 - Number of Islands
    
    INTUITION:
    Instead of exploring an island until we reach the water (like DFS or BFS), 
    we start by assuming every single piece of land ('1') is completely isolated—its 
    own distinct island. As we scan the map, whenever we find two pieces of land next 
    to each other, we build a bridge between them (a "Union"). Every time we connect 
    two previously separate islands, our total island count decreases by one. 
    By the end of the scan, we will be left with the correct number of distinct islands.
    
    APPROACH:
    1. Initializing the Disjoint Set:
       - Iterate through the grid.
       - Whenever we find land ('1'), we map its 2D coordinates (row, col) to a 1D 
         index (row * total_columns + col).
       - We record this index in our `parent` array, essentially making the cell 
         its own "root" or "parent". We also increment our `islands` counter.
       - Water cells ('0') get a placeholder (-1) in the `parent` array.
    2. Finding the Root (`find`):
       - To check which island a cell belongs to, we trace its parents up to the "root".
       - We use "Path Compression" here: once we find the root, we connect the cell 
         directly to it so future lookups are lightning fast.
    3. Connecting Islands (`union`):
       - We find the roots of the two adjacent land cells.
       - If they have different roots (meaning they were previously separate islands), 
         we connect them by making one root the parent of the other.
       - We then decrement our total `islands` count by 1.
    4. Building the Map:
       - We scan the grid a second time. 
       - For every '1', we only need to check the cell to its Right and the cell Down. 
         (Checking Left and Up is redundant because we already processed them earlier).
       - If a neighbor is also '1', we `union` them.
    5. Return the final `islands` count.
    
    COMPLEXITY:
    - Time Complexity: $O(M \times N \times \alpha(M \times N))$. We iterate over the 
      grid to initialize and then to union. The `find` and `union` operations take 
      nearly $O(1)$ time thanks to path compression, governed by the inverse Ackermann 
      function $\alpha$. For all practical purposes, this evaluates to $O(M \times N)$.
    - Space Complexity: $O(M \times N)$ explicitly used to store the `parent` array, 
      which maps out every single cell in the grid.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        # parent array to track which set a cell belongs to
        parent = []
        islands = 0
        
        # 1. Initialize the board
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # Map the 2D coordinate to a 1D index
                    parent.append(i * n + j)
                    islands += 1
                else:
                    # Water cells get a placeholder
                    parent.append(-1)
                    
        # Find the root of the set a cell belongs to (with path compression)
        def find(i: int) -> int:
            if parent[i] == i:
                return i
            # Path compression: point the node directly to the root
            parent[i] = find(parent[i])
            return parent[i]
            
        # Connect two adjacent land cells into the same set
        def union(i: int, j: int):
            nonlocal islands
            root_i = find(i)
            root_j = find(j)
            
            # If they have different roots, connect them and decrement the island count
            if root_i != root_j:
                parent[root_i] = root_j
                islands -= 1
                
        # 2. Traverse the grid and connect adjacent lands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # Only check Right and Down to avoid redundant unions
                    if j + 1 < n and grid[i][j + 1] == '1':
                        union(i * n + j, i * n + j + 1) # Right
                    if i + 1 < m and grid[i + 1][j] == '1':
                        union(i * n + j, (i + 1) * n + j) # Down
                        
        return islands