import collections
from typing import List

class Solution:
    """
    Problem: LeetCode 200 - Number of Islands
    
    INTUITION:
    Similar to DFS, we want to find a piece of land ('1') and "sink" the entire island 
    so we don't count it again. However, instead of diving deep to the end of the island 
    recursively (DFS), we will explore the island layer-by-layer (BFS) like a ripple in 
    a pond. We use a Queue to keep track of the next coordinates to check.
    
    APPROACH:
    1. Iterate through the grid looking for land ('1').
    2. Upon finding land, increment our `islands` count and start a BFS:
       a. Initialize a Queue and enqueue the starting cell's coordinates.
       b. Immediately mark the cell as '0' (visited) so it isn't added to the queue again.
       c. While the queue is not empty, pop the front cell.
       d. Check its 4 neighbors (Up, Down, Left, Right).
       e. If a neighbor is '1', mark it as '0' and push it into the queue.
    3. Return the total island count.
    
    COMPLEXITY:
    - Time Complexity: $O(M \times N)$ where M is rows and N is columns. Every cell is 
      visited and processed a constant number of times.
    - Space Complexity: $O(\min(M, N))$ for the queue. In the worst-case scenario (an 
      island filling the grid), the queue holds the expanding perimeter of the BFS. 
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        islands = 0
        
        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def bfs(r, c):
            queue = collections.deque([(r, c)])
            grid[r][c] = '0' # Sink immediately upon adding to queue
            
            while queue:
                curr_r, curr_c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    # If neighbor is valid and is land, queue it up and sink it
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0' 

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(i, j)
                    
        return islands