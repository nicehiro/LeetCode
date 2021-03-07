from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.method2(s)

    def method1(self, s):
        self.s = s
        self.res = []
        if len(s) == 0:
            return self.res
        self.recursive(0, len(s), [])
        return self.res

    def recursive(self, a, b, prev):
        if a == b:
            self.res.append(prev)
        for i in range(1, b - a + 1):
            if self.is_palindrome(self.s[a : a + i]):
                p = prev.copy()
                p.append(self.s[a : a + i])
                self.recursive(a + i, b, p)

    def is_palindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def method2(self, s: str):
        """动态规划 + DFS"""
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        res = []
        ans = []

        def dfs(i):
            if i >= n:
                res.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i : j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return res


if __name__ == "__main__":
    solu = Solution()
    s = ""
    print(solu.partition(s))
