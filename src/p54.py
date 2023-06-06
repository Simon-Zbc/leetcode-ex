from typing import List


## Runtime 14.8%
## Memory 21.1%
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        
        while l <= r and t <= b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if t <= b:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1
        return res