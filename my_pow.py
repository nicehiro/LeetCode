class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            if n % 2 == 0:
                a = self.myPow(x, n // 2)
                return a * a
            else:
                a = self.myPow(x, n // 2)
                return x * a * a
        if n == 0:
            return 1
        return 1 / self.myPow(x, -n)


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2, -2))