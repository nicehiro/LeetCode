from typing import List
from copy import deepcopy
from functools import reduce


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        m = [['x'] * n for _ in range(n)]
        self.recursive(0, n, m)
        return self.format(self.res)

    def recursive(self, i, n, m):
        if i >= n:
            self.res.append(m)
            return
        if m[i] == '.' * n:
            return
        for j in range(n):
            if m[i][j] == 'x':
                t = deepcopy(m)
                self.update_map(i, j, n, t)
                self.recursive(i + 1, n, t)

    def update_map(self, i, j, n, u):
        for k in range(n):
            u[i][k] = '.'
            u[k][j] = '.'
        u[i][j] = 'Q'
        a, b = i + 1, j + 1
        while a < n and b < n:
            u[a][b] = '.'
            a += 1
            b += 1
        a, b = i - 1, j - 1
        while a >= 0 and b >= 0:
            u[a][b] = '.'
            a -= 1
            b -= 1
        a, b = i + 1, j - 1
        while a < n and b >= 0:
            u[a][b] = '.'
            a += 1
            b -= 1
        a, b = i - 1, j + 1
        while a >= 0 and b < n:
            u[a][b] = '.'
            a -= 1
            b += 1

    def format(self, m):
        l2str = lambda x, y: x + y
        res = []
        for item in m:
            res.append([reduce(l2str, t) for t in item])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))