class Solution:
    def minCut(self, s: str) -> int:
        self.s = s
        # return self.recursive(0, len(s))
        return self.iteration()

    def recursive(self, f, e):
        if self.is_palindrome(self.s[f:e]):
            return 0
        min_cut = float('inf')
        for i in range(1, e-f):
            cut = 1 + self.recursive(f+i, e) + self.recursive(f, f+i)
            if min_cut > cut:
                min_cut = cut
        return min_cut

    def iteration(self):
        n = len(self.s)
        check_palindrome = [[False for _ in range(n)] for _ in range(n)]
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left + 1][right - 1]):
                    check_palindrome[left][right] = True
        res = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n-1):
            k, l = 0, 2+i
            while k <= n and l <= n:
                # if self.is_palindrome(self.s[k:l]):
                if check_palindrome[k][l-1]:
                    res[k][l] = 0
                else:
                    t = [res[k+i][l] + res[k][k+i] for i in range(1, l-k)]
                    res[k][l] = 1 + min(t)
                k += 1
                l += 1
        return res[0][-1]

    def is_palindrome(self, s):
        f, e = 0, len(s)-1
        while f < e:
            if s[f] != s[e]:
                return False
            f += 1
            e -= 1
        return True


if __name__ == '__main__':
    s = 'aab'
    solu = Solution()
    print(solu.minCut(s))
