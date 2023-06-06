from collections import defaultdict


## Runtime 69.9%
## Memory 39.9%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        position = defaultdict(int)
        start = 0

        for end, c in enumerate(s):
            start = max(start, position[c])
            max_len = max(max_len, end - start + 1)
            position[c] = end + 1
        
        return max_len