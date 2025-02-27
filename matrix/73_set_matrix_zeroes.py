class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Rather than track the zero rows & cols outside of the matrix,
        the top row and left column can be used as we iterate through the matrix.
        Because the top-left cell would be used by both we need a separate variable
        to track one of them, in this case I chose rows.
        Time: O(m * n), Space: O(1)
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        # Get zero rows & cols
        top_row = matrix[0][0]
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Update col tracker
                    matrix[0][c] = 0
                    # Update row tracker
                    if r == 0:
                        top_row = 0
                    else:
                        matrix[r][0] = 0

        # Set zeroes
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if top_row == 0:
            for c in range(COLS):
                matrix[0][c] = 0
