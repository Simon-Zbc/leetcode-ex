from typing import List

## Runtime 32.4%
## Memory 99.6%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(nums, target, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            if len(nums) == 1:
                if nums[0] == target:
                    res.append(path + [nums[0]])
                    return
                else:
                    return

            for i in range(len(nums)):
                if i > 0:
                    if nums[i] == nums[i - 1]:
                        continue
                dfs(nums[i+1:], target - nums[i], path + [nums[i]], res)
        
        dfs(candidates, target, [], res)
        if candidates[-1] == target and [target] not in res:
            res.append([target])
        return res