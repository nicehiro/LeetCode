from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        m, n = len(matrix), len(matrix[0])
        low_i, high_i, low_j, high_j = 0, m, 0, n
        i, j = 0, 0
        res = []
        while low_i < high_i and low_j < high_j:
            for j in range(low_j, high_j):
                res.append(matrix[i][j])
            low_i += 1
            for i in range(low_i, high_i):
                res.append(matrix[i][j])
            high_j -= 1
            if low_i >= high_i or low_j >= high_j:
                break
            for j in range(high_j - 1, low_j - 1, -1):
                res.append(matrix[i][j])
            high_i -= 1
            for i in range(high_i - 1, low_i - 1, -1):
                res.append(matrix[i][j])
            low_j += 1
        return res

    def method2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        up, left, down, right = 0, 0, m - 1, n - 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        res = []
        curr_d = 0
        while len(res) < m * n:
            res.append(matrix[x][y])
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
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [
    #             [1, 2, 3, 4],
    #             [5, 6, 7, 8],
    #             [9,10,11,12]
    #          ]
    matrix = [[7], [9], [6]]
    print(s.spiralOrder(matrix))
