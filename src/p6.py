## Runtime 33.5%
## Memory 68.5%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            res = ''
            for r in range(numRows):
                n = 2 * (numRows - 1) - 2 * r
                while r < len(s):
                    if n != 0:
                        res += s[r]
                    r += n
                    n = 2 * (numRows - 1) - n
        return res