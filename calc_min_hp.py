from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.m = len(dungeon)
        self.n = len(dungeon[0])
        self.dungeon = dungeon
        self.res = []
        # return self.get_min_hp(self.recursive(0, 0))
        return self.get_min_hp(self.iteration())

    def get_min_hp(self, hp):
        if hp >= 0:
            return 1
        return abs(hp) + 1

    def recursive(self, x, y):
        if x >= self.m or y >= self.n:
            return -float('inf')
        if x == self.m-1 and y == self.n-1:
            return self.dungeon[-1][-1]
        right = self.recursive(x, y+1)
        down = self.recursive(x+1, y)
        return min(self.dungeon[x][y], self.dungeon[x][y] + max(right, down))

    def iteration(self):
        dp = [[float('-inf') for _ in range(self.n+1)] for _ in range(self.m+1)]
        dp[-2][-2] = self.dungeon[-1][-1]
        for i in range(self.m-1, -1, -1):
            for j in range(self.n-1, -1, -1):
                if i == self.m-1 and j == self.n-1:
                    continue
                dp[i][j] = min(self.dungeon[i][j],
                               self.dungeon[i][j] + max(dp[i+1][j], dp[i][j+1]))
        return dp[0][0]



if __name__ == '__main__':
    solu = Solution()
    dungeon = [[-2, -3, 3],
               [-5, -10, 1],
               [10, 30, -5]]
    print(solu.calculateMinimumHP(dungeon))
