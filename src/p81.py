from typing import List


## Runtime 78.2%
## Memory 45.9%
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return True
            if nums[m] == nums[l] and nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[m] >= nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return False