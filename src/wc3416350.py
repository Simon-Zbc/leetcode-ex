from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        n, d = len(nums), len(divisors)
        divisors.sort()
        score, res = 0, 0
        for i in range(d):
            count = 0
            for j in range(n):
                if nums[j] % divisors[i] == 0:
                    count  += 1
            if count > score:
                score = count
                res = divisors[i]
        if res == 0:
            return divisors[0]
        else:
            return res
