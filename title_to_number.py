class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        base = 26
        for i in range(len(s)):
            res += (ord(s[len(s)-i-1]) - 64) * (base ** i)
        return res
