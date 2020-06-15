class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.l_s = len(s)
        self.l_t = len(t)
        if self.l_s < self.l_t:
            return 0
        self.s = s
        self.t = t
        # return self.recursive(0, 0)
        return self.iteration()

    def recursive(self, i, j):
        if j >= self.l_t:
            return 1
        if i >= self.l_s:
            return 0
        if self.s[i] == self.t[j]:
            return self.recursive(i+1, j+1) + self.recursive(i+1, j)
        return self.recursive(i+1, j)

    def iteration(self):
        dp = [[0 for _ in range(self.l_t+1)] for _ in range(self.l_s+1)]
        for i in range(self.l_s):
            dp[i][-1] = 1
        for i in range(self.l_t):
            dp[-1][i] = 0
        dp[-1][-1] = 1
        for i in range(self.l_s-1, -1, -1):
            for j in range(self.l_t-1, -1, -1):
                if i < j:
                    continue
                if self.s[i] == self.t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]


if __name__ == '__main__':
    solu = Solution()
    s = 'ddd'
    t = 'dd'
    print(solu.numDistinct(s, t))
