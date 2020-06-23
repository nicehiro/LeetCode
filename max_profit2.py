from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        # return max(self.recursive(0, 0, True), 0)
        return self.iteration()

    def recursive(self, i, s, c):
        if i >= len(self.prices):
            return s
        if c:
            return max(self.recursive(i+1, s-self.prices[i], False), self.recursive(i+1, s, True))
        return max(self.recursive(i+1, s+self.prices[i], True), self.recursive(i+1, s, False))

    def iteration(self):
        dp = [[0 for _ in range(len(self.prices))] for _ in range(2)]
        dp[0][-1] = 0
        dp[1][-1] = self.prices[-1]
        for j in range(len(self.prices)-2, -1, -1):
            dp[0][j] = max(dp[1][j+1]-self.prices[j], dp[0][j+1])
            dp[1][j] = max(dp[0][j+1]+self.prices[j], dp[1][j+1])
        return dp[0][0]


if __name__ == '__main__':
    solu = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solu.maxProfit(prices))