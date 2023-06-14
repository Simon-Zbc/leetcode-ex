from typing import List


## Runtime 53.5%
## Memory 51.5%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, (row * col) - 1
        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // col][mid % col]
            if num == target:
                return True
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False