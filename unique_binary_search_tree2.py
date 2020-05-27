class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        self.n = n
        # return self.recursive2(1, n+1)
        return self.iteration()

    def recursive2(self, s, e):
        if s == e:
            return 1
        if e - s == 1:
            return 1
        res = []
        for i in range(s, e):
            left = self.recursive2(s, i)
            right = self.recursive2(i+1, e)
            res.append(left * right)
        return sum(res)

    def iteration(self):
        dp = [[1 for _ in range(self.n+2)] for _ in range(self.n+2)]
        for i in range(3, self.n+2):
            a = 1
            b = i
            while b < self.n + 2:
                res = 0
                for t in range(a, b):
                    res += dp[a][t] * dp[t+1][b]
                dp[a][b] = res
                a += 1
                b += 1
        return dp[1][-1]


if __name__ == '__main__':
    solu = Solution()
    print(solu.numTrees(19))
