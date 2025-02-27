class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[-1][-1] = -1

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if r == 0 and c == 0 or obstacleGrid[r][c] == 1:
                    continue
                elif r == 0:
                    if obstacleGrid[r][c - 1] <= 0:
                        obstacleGrid[r][c - 1] += obstacleGrid[r][c]
                elif c == 0:
                    if obstacleGrid[r - 1][c] <= 0:
                        obstacleGrid[r - 1][c] += obstacleGrid[r][c]
                else:
                    if obstacleGrid[r][c - 1] <= 0:
                        obstacleGrid[r][c - 1] += obstacleGrid[r][c]
                    if obstacleGrid[r - 1][c] <= 0:
                        obstacleGrid[r - 1][c] += obstacleGrid[r][c]

        return -obstacleGrid[0][0]
