class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)
            if dp[i] == dp[index2] * 2:
                index2 += 1
            if dp[i] == dp[index3] * 3:
                index3 += 1
            if dp[i] == dp[index5] * 5:
                index5 += 1
        return dp[-1]
