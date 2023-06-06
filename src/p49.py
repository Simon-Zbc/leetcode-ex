from typing import List


## Runtime 81.8%
## Memory 93.7%
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in res:
                res[sorted_s] = []
            res[sorted_s].append(s)
        return list(res.values())