from typing import List


## Runtime 5.7%
## Memory 14.5%
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]