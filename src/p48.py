from typing import List


## Runtime 18.1%
## Memory 96.9%
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        u, d = 0, n - 1
        while u < d:
            matrix[u], matrix[d] = matrix[d], matrix[u]
            u += 1
            d -= 1
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]