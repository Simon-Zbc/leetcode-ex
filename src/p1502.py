from typing import List


## Runtime 17.1%
## Memory 57.6%
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i] + diff != arr[i+1]:
                return False
        return True