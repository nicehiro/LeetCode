class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        table = [str(x+1) for x in range(n)]
        res = ''
        for i in range(n-1, -1, -1):
            f = self.factorial(i)
            t = k // f
            k = k % f
            if k == 0:
                res += table[t-1]
                table.pop(t-1)
                for j in table[::-1]:
                    res += j
                return res
            res += table[t]
            table.pop(t)

    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        return n * self.factorial(n-1)
        

if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(4, 9))