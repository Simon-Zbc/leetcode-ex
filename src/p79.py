from typing import List


## Runtime 48.8%
## Memory 34.1%
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or col < 0 or row >=m or col >= n or word[index] != board[row][col] or (row, col) in seen:
                return False
            seen.add((row, col))
            res = (dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1))
            seen.remove((row, col))
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False