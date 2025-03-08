from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        rows = [row]
        for r in range(2, numRows + 1):
            row = [0] + row + [0]
            new_row = [row[i] + row[i+1] for i in range(r)]
            row = new_row
            rows.append(row)
        return rows
