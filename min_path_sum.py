from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        # return self.recursive(0, 0)
        return self.iteration()
        
    def iteration(self):
        res = [[0] * (self.n) for _ in range(self.m)]
        num = min(self.m, self.n) - 1
        i = self.m - 1
        j = self.n - 1
        while num >= 0:
            a, b = i, j
            while a >= 0:
                if a+1 >= self.m and j+1 >= self.n:
                    minest = 0
                elif a+1 >= self.m:
                    minest = res[a][j+1]
                elif j+1 >= self.n:
                    minest = res[a+1][j]
                else:
                    minest = min(res[a][j+1], res[a+1][j])
                res[a][j] = self.grid[a][j] + minest
                a -= 1
            while b >= 0:
                if i+1 >= self.m and b+1 >= self.n:
                    minest = 0
                elif i+1 >= self.m:
                    minest = res[i][b+1]
                elif b+1 >= self.n:
                    minest = res[i+1][b]
                else:
                    minest = min(res[i][b+1], res[i+1][b])
                res[i][b] = self.grid[i][b] + minest
                b -= 1
            num -= 1
            i -= 1
            j -= 1
        return res[0][0]
    
    def recursive(self, i, j):
        if i == self.m-1 and j == self.n-1:
            return self.grid[-1][-1]
        if i >= self.m - 1:
            b = j + 1
            return self.recursive(i, b) + self.grid[i][j]
        if j >= self.n - 1:
            a = i + 1
            return self.recursive(a, j) + self.grid[i][j]
        a = i + 1
        b = j + 1
        return min(self.recursive(i, b) + self.grid[i][j],
                   self.recursive(a, j) + self.grid[i][j])


if __name__ == "__main__":
    s = Solution()
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print(s.minPathSum(grid))
    