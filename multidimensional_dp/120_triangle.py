class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        rows = len(triangle) - 1  # zero index

        # Edit the triangle in place, bottom up
        for row in range(rows-1, -1, -1):
            for idx in range(len(triangle[row])):
                triangle[row][idx] += min(triangle[row+1][idx], triangle[row+1][idx+1])

        return triangle[0][0]