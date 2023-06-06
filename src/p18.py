from typing import List


## Runtime 50.2%
## Memory 86.6%
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        res = []
        i = 0
        while i < n - 3:
            j = i + 1
            while j < n - 2:
                l = j + 1
                r = n - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while r > l and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
                while j < n - 2 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < n - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res