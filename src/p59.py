from typing import List


## Runtime 12.9%
## Memory 10.7%
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        count = 1
        t, b, l, r = 0, n-1, 0, n-1
        while(t <= b and l <= r):
            for i in range(l, r+1):
                res[t][i] = count
                count += 1
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                res[i][r] = count
                count += 1
            r -= 1
            if l > r:
                break
            for i in range(r, l-1, -1):
                res[b][i] = count
                count += 1
            b -= 1
            if t > b:
                break
            for i in range(b, t-1, -1):
                res[i][l] = count
                count += 1
            l += 1
        return res