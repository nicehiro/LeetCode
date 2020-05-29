class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s3) == 0:
            return True
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        # return self.recursive(0, 0, 0)
        return self.iteration()

    def recursive(self, i, j, k):
        if i >= len(self.s1) and j >= len(self.s2) and k >= len(self.s3):
            return True
        if i < len(self.s1) and j < len(self.s2):
            if self.s1[i] == self.s3[k] and self.s2[j] == self.s3[k]:
                return self.recursive(i+1, j, k+1) or self.recursive(i, j+1, k+1)
            if self.s1[i] == self.s3[k]:
                return self.recursive(i+1, j, k+1)
            if self.s2[j] == self.s3[k]:
                return self.recursive(i, j+1, k+1)
            return False
        if i < len(self.s1) and self.s1[i] == self.s3[k]:
            return self.recursive(i+1, j, k+1)
        if j < len(self.s2) and self.s2[j] == self.s3[k]:
            return self.recursive(i, j+1, k+1)
        return False

    def iteration(self):
        dp = [[False for _ in range(len(self.s2))] for _ in range(len(self.s1))]
        for i in range(len(self.s1)):
            for j in range(len(self.s2)):
                if self.s1[i] == self.s3[i+j+1] and self.s2[j] == self.s3[i+j+1]:
                    if i-1 >= 0 and j-1 >= 0:
                        dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    elif i-1 >= 0:
                        dp[i][j] = dp[i-1][j]
                    elif j-1 >= 0:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = self.s1[i] == self.s3[i+j] or self.s2[j] == self.s3[i+j]
                elif self.s1[i] == self.s3[i+j+1]:
                    if i-1 >= 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = self.s2[j] == self.s3[i+j]
                elif self.s2[j] == self.s3[i+j+1]:
                    if j-1 >= 0:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = self.s1[i] == self.s3[i+j]
        return dp[-1][-1]


if __name__ == '__main__':
    solu = Solution()
    s1 = 'db'
    s2 = 'b'
    s3 = 'cbb'
    print(solu.isInterleave(s1, s2, s3))
