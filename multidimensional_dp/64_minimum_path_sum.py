class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Edit the grid in place, "bottom up"
        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                if row + 1 < ROWS and col + 1 < COLS:
                    grid[row][col] += min(grid[row+1][col], grid[row][col+1])
                elif row + 1 < ROWS:
                    grid[row][col] += grid[row+1][col]
                elif col + 1 < COLS:
                    grid[row][col] += grid[row][col+1]
        
        # The minimum path sum is stored in the top left corner of the grid
        return grid[0][0]