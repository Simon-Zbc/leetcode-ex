import math
from typing import List


## Runtime 47.5%
## Memory 75.2%
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        l = len(potions)
        potions.sort()
        res = []
        for s in spells:
            left, right = 0, l - 1
            target = math.ceil(success / s)
            while left <= right:
                m = (left + right) // 2
                if potions[m] < target:
                    left = m + 1
                else:
                    right = m - 1
            res.append(l - left)
        return res