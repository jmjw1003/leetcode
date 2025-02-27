class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Edit grid in-place to save on memory.
        Alternatively you could use a hash set of visited island locations.
        """
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0

        def explore(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                explore(row + dr, col + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num_islands += 1
                    explore(r, c)

        return num_islands