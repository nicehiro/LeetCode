from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(s.transpose(matrix))
