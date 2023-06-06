from typing import List


## Runtime 12.5%
## Memory 59.1%
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 3:
            nums.reverse()
        else:
            for i in range(l):
                if nums[l - i - 1] > nums[l - i - 2]:
                    nums[l - i - 1:] = sorted(nums[l - i - 1:])
                    for j in range(l - i - 1, l):
                        if nums[j] > nums[l - i - 2]:
                            nums[j], nums[l - i - 2] = nums[l - i - 2], nums[j]
                            break
                    break