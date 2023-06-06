from typing import List


## Runtime 38.5%
## Memory 45.3%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = -10 ** 4
        max_v = 0
        for num in nums:
            max_v += num
            res = max(res, max_v)
            max_v = max(max_v, 0)
        return res