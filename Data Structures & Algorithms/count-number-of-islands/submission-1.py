from pprint import pprint

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) if grid else 0
        result = 0

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return 0

            if grid[r][c] != "1":
                return 0
            
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return 1

        for r in range(ROWS):
            for c in range(COLS):
                result += dfs(r, c)
        return result