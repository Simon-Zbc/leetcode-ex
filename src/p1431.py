from typing import List


## Runtime 82.3%
## Memory 95.2%
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_v = max(candies)
        return [i + extraCandies >= max_v for i in candies]