from typing import List


## Runtime 49.5%
## Memory 89.8%
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        for l in range(n - 2):
            if l == 0 or nums[l] != nums[l - 1]:
                m = l + 1
                r = n - 1
                if l == 0:
                    min_sum = nums[l] + nums[m] + nums[r]
                while m < r:
                    sum = nums[l] + nums[m] + nums[r]
                    if sum == target:
                        return target
                    elif sum > target:
                        r -= 1
                    else:
                        m += 1
                    if abs(sum - target) < abs(min_sum - target):
                        min_sum = sum
        return min_sum