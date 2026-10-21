class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        number_islands = 0

        def dfs(r, c):
            # Stop if out of bounds or this cell is water/already visited.
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return

            # Mark visited before exploring neighbors.
            grid[r][c] = "0"

            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    number_islands += 1
                    dfs(r, c)

        return number_islands