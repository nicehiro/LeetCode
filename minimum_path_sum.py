from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        # return self.recursive(0, 0, 0)
        return self.iteration()

    def recursive(self, n: int, m: int, s: int):
        if n >= len(self.triangle):
            return s
        if m > n:
            return s
        return min(self.recursive(n+1, m, s+self.triangle[n][m]),
                   self.recursive(n+1, m+1, s+self.triangle[n][m]))

    def iteration(self):
        n = len(self.triangle)
        temp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                temp[j] = self.triangle[i][j] + min(temp[j], temp[j+1])
        return temp[0]


if __name__ == '__main__':
    solu = Solution()
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(solu.minimumTotal(triangle))