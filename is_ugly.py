class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        res = True
        while n > 1 and res:
            res = False
            for k in [2, 3, 5]:
                if n % k == 0:
                    n //= k
                    res = True
                    break
        return res


if __name__ == "__main__":
    s = Solution()
    n = -2147483648
    print(s.isUgly(n))
