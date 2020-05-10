from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        self.heights = [0 for _ in matrix[0]]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    self.heights[j] += 1
                else:
                    self.heights[j] = 0
            max_area = max(max_area, self.STACK())
        return max_area

    def STACK(self):
        l = [(-1, -1)]
        res = 0
        for i in range(len(self.heights)):
            if self.heights[i] > l[-1][1]:
                l.append((i, self.heights[i]))
            else:
                while self.heights[i] <= l[-1][1]:
                    top, height = l.pop()
                    t = height * (i - l[-1][0] - 1)
                    res = t if res < t else res
                l.append((i, self.heights[i]))
        for i in range(len(l)-1, 0, -1):
            res = max((len(self.heights) - l[i-1][0] - 1) * l[i][1], res)
        return res


if __name__ == '__main__':
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]
    solu = Solution()
    print(solu.maximalRectangle(matrix))
