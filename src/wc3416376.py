from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        count = 0
        res = [0, 0]
        for i in range(m):
            if mat[i].count(1) > count:
                count = mat[i].count(1)
                res[0], res[1] = i, count
        return res

s = Solution()
print(s.rowAndMaximumOnes([[0,1],[1,0]]))
print(s.rowAndMaximumOnes([[0,0,0],[0,1,1]]))
print(s.rowAndMaximumOnes([[0,0],[1,1],[0,0]]))
print(s.rowAndMaximumOnes([[1,1],[0,0],[1,1]]))
print(s.rowAndMaximumOnes([[0],[0]]))