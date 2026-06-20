from typing import List

class Solution:
    """
    Problem: LeetCode 200 - Number of Islands
    
    INTUITION:
    Think of the grid as a map of the ocean ('0') and land ('1'). As we scan the map 
    from top-left to bottom-right, every time we encounter a '1', we have discovered 
    a completely new island. However, to avoid counting the same island multiple times 
    when we check its connected parts later, we need a way to mark it as "seen". 
    The easiest way to do this is to "sink" the island—turning every connected '1' into 
    a '0' using a Depth-First Search (DFS).
    
    APPROACH:
    1. Iterate through every cell in the m x n grid using nested loops.
    2. When a piece of land ('1') is found:
       a. Increment the `islands` counter.
       b. Trigger a DFS starting from that cell.
    3. The DFS will:
       a. Check for out-of-bounds or water ('0') cells and return immediately if found.
       b. Mutate the current cell from '1' to '0' to mark it as visited (optimizing space).
       c. Recursively call itself in all 4 valid directions (Up, Down, Left, Right).
    4. Once the nested loops finish, return the total island count.
    
    COMPLEXITY:
    - Time Complexity: $O(M \times N)$ where M is rows and N is columns. We visit every 
      cell at least once. During the DFS, we visit each land cell a constant number of times.
    - Space Complexity: $O(M \times N)$ in the worst-case scenario (a grid filled entirely 
      with land) due to the depth of the recursive call stack. However, by mutating the 
      grid directly, we save the $O(M \times N)$ auxiliary space that a separate `visited` 
      matrix would have consumed.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)      # Number of rows
        m = len(grid[0])   # Number of columns
        islands = 0
        
        def dfs(r: int, c: int):
            # Base cases: out of bounds or current cell is water/already visited
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == '0':
                return
            
            # Sink the land to prevent revisiting
            grid[r][c] = '0'
            
            # Explore the 4 adjacent horizontal and vertical directions
            dfs(r - 1, c) # Up
            dfs(r + 1, c) # Down
            dfs(r, c - 1) # Left
            dfs(r, c + 1) # Right

        # Scan the entire grid
        for i in range(n):
            for j in range(m):
                # If unvisited land is found, it's a new island
                if grid[i][j] == '1':
                    islands += 1
                    # Sink all connected land for this island
                    dfs(i, j) 
                    
        return islands