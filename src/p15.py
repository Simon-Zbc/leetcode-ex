from typing import List


## Runtime 54.4%
## Memory 38.3%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for l in range(n-2):
            if l == 0 or nums[l] != nums[l-1]:
                r = n - 1
                m = l + 1
                while r > m:
                    sum = nums[l] + nums[m] + nums[r]
                    if sum == 0:
                        res.append([nums[l], nums[m], nums[r]])
                        while m < r and nums[m] == nums[m+1]:
                            m += 1
                        while r > m and nums[r] == nums[r-1]:
                            r -= 1
                        m += 1
                        r -= 1
                    elif sum < 0:
                        m += 1
                    else:
                        r -= 1
        return res