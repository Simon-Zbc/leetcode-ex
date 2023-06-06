from typing import List


## Runtime 43.1%
## Memory 49.2%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[res] = nums[i + 1]
                res += 1
        return res