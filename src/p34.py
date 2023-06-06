from typing import List

## Runtime 99.9%
## Memory 85.8%
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l == 0:
            return [-1, -1]
        
        def search(t):
            left, right = 0, l
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < t:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        start = search(target)
        end = search(target + 1) - 1

        if start <= end:
            return [start, end]
        else:
            return [-1, -1]