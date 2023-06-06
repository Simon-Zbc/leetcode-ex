from typing import List


## Runtime 70.9%
## Memory 41.6%
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        position = l - 1
        for i in range(l - 2, -1, -1):
            if i + nums[i] >= position:
                position = i
        return position == 0