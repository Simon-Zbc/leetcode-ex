from typing import List


## Runtime 28.6%
## Memory 7.7%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for n in digits:
            s += str(n)
        temp = str(int(s) + 1)
        return [int(temp[i]) for i in range(len(temp))]