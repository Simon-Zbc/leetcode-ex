## Runtime 37.8%
## Memory 6.4%
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        def solve(row, col):
            if row == 1 or col == 1:
                return 1
            if dp[row][col]:
                return dp[row][col]
            up = solve(row - 1, col)
            left = solve(row, col - 1)
            dp[row][col] = up + left
            return dp[row][col]
        return solve(m, n)