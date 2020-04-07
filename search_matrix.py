from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if target <= matrix[i][n-1]:
                for j in range(n):
                    if target == matrix[i][j]:
                        return True
                return False
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    print(s.searchMatrix(matrix, 13))