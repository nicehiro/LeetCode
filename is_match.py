class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        last_s = last_p = ''
        while i < len(s) and j < len(p):
            if s[i] == p[j] or p[j] == '.':
                last_s = s[i]
                last_p = p[j]
                i += 1
                j += 1
            elif p[j] == '*':
                if last_p == '.':
                    while i < len(s) and s[i] == last_s:
                        i += 1
                else:
                    while i < len(s) and s[i] == last_p:
                        i += 1
                j += 1
            else:
                if p[j+1] == '*':
                    j += 2
        if i >= len(s) and j >= len(p):
            return 'true'
        return 'false'


if __name__ == '__main__':
    s = Solution()
    st = 'aa'
    p = 'a'
    print(s.isMatch(st, p))
