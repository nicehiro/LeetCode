class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        prefix = 1
        if (dividend < 0 and divisor > 0) or\
            (dividend > 0 and divisor < 0):
            prefix = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            r, dividend = self.divide_iter(dividend, divisor)
            res += r

        if prefix < 0:
            res = ~res + 1

        if res < - 2 ** 31:
            return - 2 ** 31
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        return res
        
    def divide_iter(self, dividend, divisor):
        res = 0
        i = 1
        while dividend >= divisor:
            res += i
            dividend -= divisor
            divisor += divisor
            i += i
        return res, dividend


if __name__ == '__main__':
    s = Solution()
    print(s.divide(-10, 1))