class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.recursive(n)
        return self.iteration(n)

    def recursive(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.recursive(n-1) + self.recursive(n-2)

    def iteration(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        opt = [0 for _ in range(n+1)]
        opt[1] = 1
        opt[2] = 2
        i = 3
        while i <= n:
            opt[i] = opt[i-1] + opt[i-2]
            i += 1
        return opt[n]


if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.climbStairs(n))