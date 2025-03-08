from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] # rowIndex = 0

        for r in range(1, rowIndex + 1):
            prev_row = [0] + row + [0]
            row = [prev_row[i] + prev_row[i + 1] for i in range(r + 1)]
        
        return row
