from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return self.method2(n)

    def method1(self, n):
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
                res[i][end_j - 1] = x
                x += 1
            end_j -= 1
            if start_j >= end_j:
                break
            for j in range(end_j - 1, start_j - 1, -1):
                res[end_i - 1][j] = x
                x += 1
            end_i -= 1
            for i in range(end_i - 1, start_i - 1, -1):
                res[i][start_j] = x
                x += 1
            start_j += 1
        return res

    def method2(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        up, down, left, right = 0, n - 1, 0, n - 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        x, y = 0, 0
        curr_d = 0
        i = 1
        while i <= n * n:
            res[x][y] = i
            i += 1
            if curr_d == 0 and y == right:
                up += 1
                curr_d += 1
            elif curr_d == 1 and x == down:
                right -= 1
                curr_d += 1
            elif curr_d == 2 and y == left:
                down -= 1
                curr_d += 1
            elif curr_d == 3 and x == up:
                left += 1
                curr_d += 1
            curr_d %= 4
            x += dirs[curr_d][0]
            y += dirs[curr_d][1]
        return res


if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.generateMatrix(n))
