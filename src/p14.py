from typing import List


## Runtime 93.9%
## Memory 36.9%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_min, str_max = min(strs), max(strs)
        n = min(len(str_min), len(str_max))
        i = 0
        res = ''

        while i < n:
            if str_min[i] == str_max[i]:
                res += str_min[i]
            else:
                break
            i += 1
        return res