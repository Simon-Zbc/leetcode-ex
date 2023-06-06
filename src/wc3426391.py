class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = 0
        for num in range(1, n + 1):
            if num % 3 == 0:
                res += num
            elif num % 5 == 0:
                res += num
            elif num % 7 == 0:
                res += num
        return res