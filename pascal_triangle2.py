from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        if rowIndex == 0:
            return res
        i = 1
        while i < rowIndex:
            j = i
            t = rowIndex
            up = 1
            down = 1
            while j > 0:
                up *= t
                t -= 1
                down *= j
                j -= 1
            res.append(up // down)
            i += 1
        res.append(1)
        return res
