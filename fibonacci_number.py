class Solution:
    def fib(self, n: int) -> int:
        return self.iteration(n)

    def recursive(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.recursive(n-1) + self.recursive(n-2)

    def iteration(self, n: int) -> int:
        h = [0, 1]
        for i in range(2, n+1):
            h.append(h[i-1] + h[i-2])
        return h[n]


if __name__ == '__main__':
    n = 3
    solu = Solution()
    print(solu.fib(n))
