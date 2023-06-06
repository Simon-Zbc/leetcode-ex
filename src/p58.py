## Runtime 31.5%
## Memory 6.4%
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1])