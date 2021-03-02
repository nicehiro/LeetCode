from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.sums = [0]
        else:
            m, n = len(matrix), len(matrix[0])
            self.sums = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    self.sums[i][j] = (
                        self.sums[i - 1][j]
                        + self.sums[i][j - 1]
                        - self.sums[i - 1][j - 1]
                        + matrix[i - 1][j - 1]
                    )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sums[row2 + 1][col2 + 1]
            + self.sums[row1][col1]
            - self.sums[row1][col2 + 1]
            - self.sums[row2 + 1][col1]
        )


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]

    obj = NumMatrix(matrix)
    print(obj.sumRegion(1, 1, 2, 2))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
