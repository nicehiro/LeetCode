class Solution:
    def convertToTitle(self, n: int) -> str:
        base = 26
        res = ''
        while n != 0:
            if n % base == 0:
                res = 'Z' + res
                n = (n // base) - 1
            else:
                res = chr(64 + n % base) + res
                n = n // base
        return res


if __name__ == '__main__':
    solu = Solution()
    print(solu.convertToTitle(1))
