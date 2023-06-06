## Runtime 83.9%
## Memory 97.8%
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = len(range(0, dividend - divisor + 1, divisor))
        min_limit = -(2 ** 31)
        max_limit = 2 ** 31 - 1
        if sign == -1:
            res = -res
        if res <= min_limit:
            return -(2 ** 31)
        elif res >= max_limit:
            return (2 ** 31 - 1)
        else:
            return res