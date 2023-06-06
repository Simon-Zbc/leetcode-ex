from typing import List


## Runtime 67.1%
## Memory 36.4%
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        res = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = max(res[i][j-1], res[i-1][j])
        return res[i][j]