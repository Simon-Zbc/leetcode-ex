from typing import List


## Runtime 84.4%
## Memory 49.4%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums)
        j = 0
        while j < i:
            if nums[j] == val:
                del nums[j]
                i -= 1
            else:
                j += 1
        return i