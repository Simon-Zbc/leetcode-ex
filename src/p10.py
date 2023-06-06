import re


## Runtime 15.1%
## Memory 86.6%
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = re.match(p, s)
        if res and res.group(0) == s:
            return True
        else:
            return False