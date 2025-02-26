class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        res = []

        while left < right and top < bottom:
            # Top row, left -> right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # Right col, top -> bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check that we are not overlapping
            if not (left < right and top < bottom):
                break
            
            # Bottom row, right -> left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
        
            # Left row, bottom -> top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
