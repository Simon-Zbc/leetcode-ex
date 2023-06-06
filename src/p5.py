## Runtime 74.1%
## Memory 54.1%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.palindromeAt(i, s, i), self.palindromeAt(i, s, i+1), res, key=len)
        return res

    def palindromeAt(self, l, s, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]