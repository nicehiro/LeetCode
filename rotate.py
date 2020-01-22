from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        l = n // 2
        for i in range(l):
            for j in range(i, n - 1 - i):
                t = matrix[i][j]
                x, y = i, j
                for _ in range(4):
                    x, y = y, n - x - 1
                    a = matrix[x][y]
                    matrix[x][y] = t
                    t = a
        return matrix
                

if __name__ == "__main__":
    s = Solution()
    # matrix = [
    #             [1,2,3],
    #             [4,5,6],
    #             [7,8,9]
    #          ]
    matrix = [
                [ 5, 1, 9,11],
                [ 2, 4, 8,10],
                [13, 3, 6, 7],
                [15,14,12,16]
             ]
    print(s.rotate(matrix))