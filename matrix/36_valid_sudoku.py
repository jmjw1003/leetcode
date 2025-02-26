class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for element in row:
                if element.isdigit():
                    if element in seen:
                        return False
                    seen.add(element)
        
        # Check cols
        for j in range(9):
            seen = set()
            for i in range(9):
                element = board[i][j]
                if element.isdigit():
                    if element in seen:
                        return False
                    seen.add(element)

        # Check squares
        top_lefts = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]
        for i, j in top_lefts:
            seen = set()
            for di in range(3):
                for dj in range(3):
                    element = board[i + di][j + dj]
                    if element.isdigit():
                        if element in seen:
                            return False
                        seen.add(element)
        
        return True
