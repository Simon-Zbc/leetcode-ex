## Runtime 64.1%
## Memory 50.5%
class Solution:
    def reverse(self, x: int) -> int:
        neFlg = False
        s = str(x)
        if s[0] == '-':
            s = s[1:]
            neFlg = True
        res = s[::-1]
        if neFlg:
            res = '-' + res
        res = int(res)
        if -2**31 <= res <= 2**31 - 1:
            return res
        else:
            return 0