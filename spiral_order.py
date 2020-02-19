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
            for j in range(high_j-1, low_j-1, -1):
                res.append(matrix[i][j])
            high_i -= 1
            for i in range(high_i-1, low_i-1, -1):
                res.append(matrix[i][j])
            low_j += 1
        return res


if __name__ == "__main__":
    s = Solution()
    matrix = [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ]
             ]
    # matrix = [
    #             [1, 2, 3, 4],
    #             [5, 6, 7, 8],
    #             [9,10,11,12]
    #          ]
    matrix = [[7],
              [9],
              [6]]
    print(s.spiralOrder(matrix))