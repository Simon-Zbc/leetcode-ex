## Runtime 35.8%
## Memory 99.7%
class Solution:
    def partitionString(self, s: str) -> int:
        l = len(s)
        count, left = 1, 0
        d = {}
        while left < l:
            if s[left] not in d:
                d[s[left]] = s[left]
            else:
                d.clear()
                d[s[left]] = s[left]
                count += 1
            left += 1
        return count
            