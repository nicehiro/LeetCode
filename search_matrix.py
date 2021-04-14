from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.method3(matrix, target)

    def method1(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if target <= matrix[i][n - 1]:
                for j in range(n):
                    if target == matrix[i][j]:
                        return True
                return False
        return False

    def method2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        while l < r:
            mid = (l + r + 1) // 2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid - 1
        mid = (l + r) // 2
        row = mid
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False

    def method3(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    matrix = [[1, 1]]
    print(s.searchMatrix(matrix, 13))
