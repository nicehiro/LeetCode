from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.res = []
        if len(s) == 0:
            return self.res
        self.recursive(0, len(s), [])
        return self.res

    def recursive(self, a, b, prev):
        if a == b:
            self.res.append(prev)
        for i in range(1, b-a+1):
            if self.is_palindrome(self.s[a:a+i]):
                p = prev.copy()
                p.append(self.s[a:a+i])
                self.recursive(a+i, b, p)

    def is_palindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    solu = Solution()
    s = ''
    print(solu.partition(s))
