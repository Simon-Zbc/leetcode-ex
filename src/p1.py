from typing import List

## Runtime 94.6%
## Memory 36.6%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looked = {}
        for index, value in enumerate(nums):
            var = target - nums[index]

            if var in looked:
                return [looked[var], index]
            
            looked[value] = index