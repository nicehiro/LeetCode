class Solution:
    def minCut(self, s: str) -> int:
        self.s = s
        # return self.recursive(0, len(s))
        # return self.iteration()
        return self.method3(s)

    def recursive(self, f, e):
        if self.is_palindrome(self.s[f:e]):
            return 0
        min_cut = float("inf")
        for i in range(1, e - f):
            cut = 1 + self.recursive(f + i, e) + self.recursive(f, f + i)
            if min_cut > cut:
                min_cut = cut
        return min_cut

    def iteration(self):
        n = len(self.s)
        check_palindrome = [[False for _ in range(n)] for _ in range(n)]
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (
                    right - left <= 2 or check_palindrome[left + 1][right - 1]
                ):
                    check_palindrome[left][right] = True
        res = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n - 1):
            k, l = 0, 2 + i
            while k <= n and l <= n:
                # if self.is_palindrome(self.s[k:l]):
                if check_palindrome[k][l - 1]:
                    res[k][l] = 0
                else:
                    t = [res[k + i][l] + res[k][k + i] for i in range(1, l - k)]
                    res[k][l] = 1 + min(t)
                k += 1
                l += 1
        return res[0][-1]

    def is_palindrome(self, s):
        f, e = 0, len(s) - 1
        while f < e:
            if s[f] != s[e]:
                return False
            f += 1
            e -= 1
        return True

    def method2(self, s: str):
        """动态规划 + DFS"""
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        def dfs(i):
            if i >= n:
                return 0
            if f[i][n - 1]:
                return 0

            t = 2 ** 32
            for j in range(i, n):
                if f[i][j]:
                    t = min(t, 1 + dfs(j + 1))
            return t

        return dfs(0)

    def method3(self, s: str):
        """动态规划 + 动态规划"""
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        g = [float("inf") for _ in range(n)]
        for i in range(n):
            if f[0][i]:
                g[i] = 0
            else:
                for j in range(i + 1):
                    if f[j][i]:
                        g[i] = min(g[i], g[j - 1] + 1)
        return g[-1]


if __name__ == "__main__":
    s = "aab"
    solu = Solution()
    print(solu.minCut(s))
