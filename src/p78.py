from typing import List


## Runtime 9.6%
## Memory 30.7%
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, subset):
            res.append(subset[::])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()
        dfs(0, [])
        return res