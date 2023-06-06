from typing import List

## Runtime 38.9%
## Memory 70.2%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = [set() for x in range(9)], [set() for x in range(9)]
        squs = [[set() for x in range(3)] for y in range(3)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in rows[i] or cell in cols[j] or cell in squs[i//3][j//3]:
                    return False
                rows[i].add(cell)
                cols[j].add(cell)
                squs[i//3][j//3].add(cell)
        
        return True