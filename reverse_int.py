class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        value = abs(x)
        res = 0
        max_int = 2 ** 31
        min_int = -1 * 2** 31 -1
        while value != 0:
            p = value % 10
            if res > max_int/10 or (res == max_int/10 and p > max_int%10):
                return 0
            if res < min_int/10 or (res == min_int/10 and p < min_int%10):
                return 0
            res = res * 10 + p
            value //= 10
        return res * sign


if __name__ == '__main__':
    x = -123
    s = Solution()
    print(s.reverse(x))
