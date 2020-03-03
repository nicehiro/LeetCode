from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        i, j = 0, 0
        start_i, end_i, start_j, end_j = 0, n, 0, n
        x = 1
        while i < n / 2:
            for j in range(start_j, end_j, 1):
                res[start_i][j] = x
                x += 1
            start_i += 1
            if start_i >= end_i:
                break
            for i in range(start_i, end_i, 1):
                res[i][end_j-1] = x
                x += 1
            end_j -= 1
            if start_j >= end_j:
                break
            for j in range(end_j-1, start_j-1, -1):
                res[end_i-1][j] = x
                x += 1
            end_i -= 1
            for i in range(end_i-1, start_i-1, -1):
                res[i][start_j] = x
                x += 1
            start_j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.generateMatrix(n))
