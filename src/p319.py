import math


## Runtime 8.4%
## Memory 34.9%
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))