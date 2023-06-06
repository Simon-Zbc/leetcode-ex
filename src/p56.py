from typing import List


## Runtime 89.1%
## Memory 32.1%
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i, j in intervals[1:]:
            if res[-1][1] >= i:
                res[-1][1] = max(res[-1][1], j)
            else:
                res.append([i, j])
        return res