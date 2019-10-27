from functools import reduce


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        res = [''] * numRows
        a = 2 * numRows - 2
        for i in range(length):
            index = i % a
            if index > numRows - 1:
                index = a - index
            res[index] += s[i]
        res = reduce(lambda x, y: x + y, res)
        return res


if __name__ == '__main__':
    s = Solution()
    st = 'paypalishiring'
    n = 4
    print(s.convert(st, n))
