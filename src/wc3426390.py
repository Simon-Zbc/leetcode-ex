from typing import List

# TODO timeout
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        l = len(nums)
        for i in range(l - k + 1):
            subarr = sorted(nums[i:i+k])
            res.append(subarr[x - 1] if subarr[x - 1] < 0 else 0)
        return res