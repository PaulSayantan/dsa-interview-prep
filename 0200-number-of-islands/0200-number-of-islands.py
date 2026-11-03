class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        n = len(grid[0])
        m = len(grid)
        visited = [[0] * n for _ in range(m)]
        count = 0
        dx = 0, 1, 0, -1
        dy = -1, 0, 1, 0 
        def perform_bfs(grid, visited, i, j):
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            while len(queue) != 0:
                x, y = queue.pop()
                for p, q in zip(dx, dy):
                    mx = x + p
                    ny = y + q
                    if 0 <= mx < m and 0 <= ny < n and grid[mx][ny] == '1' and not visited[mx][ny]:
                        queue.append((mx, ny))
                        visited[mx][ny] = 1
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    perform_bfs(grid, visited, i, j)
                    count += 1

        return count
                
