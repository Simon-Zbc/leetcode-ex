from typing import List


## Runtime 70.9%
## Memory 94.1%
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones:
            stones.sort()
            y = stones.pop()
            if not stones:
                return y
            x = stones.pop()
            if y > x:
                stones.append(y - x)
        return 0