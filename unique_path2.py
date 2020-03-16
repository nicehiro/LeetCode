from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # return self.recursive(1, 1, m, n)
        self.grid = obstacleGrid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.iteration(m, n)

    def recursive(self, x, y, m, n):
        if x < m and y < n:
            return self.recursive(x + 1, y, m, n) + self.recursive(x, y + 1, m, n)
        if x < m:
            return self.recursive(x + 1, y, m, n)
        if y < n:
            return self.recursive(x, y + 1, m, n)
        else:
            return 1

    def iteration(self, m, n):
        res = [[0] * (n+1) for _ in range(m+1)]
        res[0][1] = 1
        i = 1
        while i < min(m+1, n+1):
            for j in range(i, m+1):
                if self.grid[j-1][i-1] == 1:
                    res[j][i] = 0
                else:
                    res[j][i] = res[j-1][i] + res[j][i-1]
            for j in range(i, n+1):
                if self.grid[i-1][j-1] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
            i += 1
        return res[m][n]


if __name__ == '__main__':
    s = Solution()
    grid = [[0,0,0],
            [0,1,0],
            [0,0,0]]
    print(s.uniquePathsWithObstacles(grid))
