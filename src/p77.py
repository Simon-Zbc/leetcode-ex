from typing import List


## Runtime 48.7%
## Memory 27.5%
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(start, cur_combine):
            if len(cur_combine) == k:
                res.append(cur_combine[::])
                return
            else:
                for i in range(start, n + 1):
                    cur_combine.append(i)
                    dfs(i + 1, cur_combine)
                    cur_combine.pop()
                return
        dfs(1, [])
        return res