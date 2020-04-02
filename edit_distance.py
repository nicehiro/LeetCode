class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        res = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            res[i][0] = i
        for i in range(n+1):
            res[0][i] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                res[i][j] = res[i-1][j-1] if word1[i-1] == word2[j-1] else 1 + min(res[i-1][j-1], res[i-1][j], res[i][j-1])
        return res[m][n]


if __name__ == "__main__":
    s = Solution()
    word1 = 'horse'
    word2 = 'ros'
    print(s.minDistance(word1, word2))