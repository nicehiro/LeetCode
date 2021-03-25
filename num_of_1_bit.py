class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.method2(n)

    def method1(self, n):
        return sum(1 for i in range(32) if n & (i << 1))

    def method2(self, n):
        res = 0
        while n != 0:
            res += 1
            n = n & (n - 1)
        return res
