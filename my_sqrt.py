class Solution:
    def mySqrt(self, x: int) -> int:
        return self.newton(x)

    def iteration(self, x):
        if x == 0:
            return 0
        if x <= 2:
            return 1
        for i in range(1, x):
            if i * i == x:
                return i
            if i * i > x:
                return i - 1

    def newton(self, x):
        # x_{n+1} = x_{n} - \frac{x_{n}^{2} - a}{2 x_n}
        x_n = x + 2
        x_n_ = x
        while abs(x_n - x_n_) > 1:
            x_n = x_n_
            x_n_ = x_n - (x_n * x_n - x) / (2 * x_n)
        return int(x_n_)


if __name__ == "__main__":
    s = Solution()
    x = 10
    print(s.mySqrt(x))