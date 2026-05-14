from pprint import pprint

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) if grid else 0
        result = 0

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return

            if grid[r][c] != "1":
                return False
            
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return True


        pprint(grid)
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c):
                    result += 1
                    print(r, c)
                    pprint(grid)
        return result