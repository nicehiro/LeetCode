from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for n in range(3, numRows+1):
            temp = [1]
            i = 1
            while i < n-1:
                a = res[n-2][i] + res[n-2][i-1]
                temp.append(a)
                i += 1
            temp.append(1)
            res.append(temp)
        return res
