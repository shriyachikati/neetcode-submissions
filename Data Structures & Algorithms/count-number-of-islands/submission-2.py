class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLUMNS = len(grid), len(grid[0])
        output = 0

        def dfs(r, c):
            # If the index is out of bounds or if it is water, we return
            if (r < 0) or (c < 0) or (r >= ROWS) or (c >= COLUMNS) or (grid[r][c] == "0"):
                return

            # We mark the piece of land as seen as it was already counted towards being piece of an island
            grid[r][c] = "0"

            # Check all four directions to see if they are also pieces of land
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Loop through the grid to find land
        for r in range(ROWS):
            for c in range(COLUMNS):
                # If it is land, we run DFS on it
                if grid[r][c] == "1":
                    dfs(r, c)
                    output += 1

        return output