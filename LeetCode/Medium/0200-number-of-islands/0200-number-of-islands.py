class Solution:
    def __init__(self):
        self.dr = [-1, 1, 0, 0]
        self.dc = [0, 0, -1, 1]

    def isValidCell(self, grid: List[List[str]], nr: int, nc: int, visited: List[List[bool]]):
        n = len(grid)
        m = len(grid[0])

        return 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and not visited[nr][nc]

    def dfs(self, grid: List[List[str]], row: int, col: int, visited: List[List[bool]]):
        visited[row][col] = True

        for k in range(4):
            n_row = row + self.dr[k]
            n_col = col + self.dc[k]

            if self.isValidCell(grid, n_row, n_col, visited):
                self.dfs(grid, n_row, n_col, visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) # row
        m = len(grid[0]) # col

        visited = [[False for _ in range(m)] for _ in range(n)]

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, i, j, visited)
                    islands += 1

        return islands