from functools import reduce


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.match_iteration(s, p)

    def match_recursive(self, s, p, i, j):
        """Recursive method.
        Runs failed cause time out.
        """
        if i >= len(s) and j >= len(p):
            return True
        if i >= len(s) and j < len(p):
            return reduce(lambda x, y: x and y, \
                [True if x == '*' else False for x in p[j:]])
        if i < len(s) and j >= len(p):
            return False
        if s[i] == p[j] or p[j] == '?':
            return self.match_recursive(s, p, i+1, j+1)
        if p[j] != '*' and s[i] != p[j]:
            return False
        return self.match_recursive(s, p, i, j+1) or\
            self.match_recursive(s, p, i+1, j) or\
                self.match_recursive(s, p, i+1, j+1)

    def match_iteration(self, s, p):
        """Iteration method.
        """
        if len(s) == 0:
            if len(p) == 0 or p == '*':
                return True
            else:
                return False
        if len(p) == 0:
            return False
        res = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        res[len(p)][len(s)] = True
        for i in range(len(p)-1, -1, -1):
            if p[i] == '*':
                res[i][len(s)] = True
            else:
                break
        def judge(i, j):
            if s[i] == p[j] or p[j] == '?':
                return res[j+1][i+1]
            if p[j] == '*':
                return res[j][i+1] or res[j+1][i] or res[j+1][i+1]
            return False
        for i in range(len(s)-1, -1, -1):
            res[len(p)-1][i] = judge(i, len(p)-1)
        for j in range(len(p)-1, -1, -1):
            res[j][len(s)-1] = judge(len(s)-1, j)
        for j in range(len(p)-2, -1, -1):
            for i in range(len(s)-2, -1, -1):
                res[j][i] = judge(i, j)
        return res[0][0]
        

if __name__ == "__main__":
    s = Solution()
    # s_ = "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab"
    # p = "***bba**a*bbba**aab**b"
    s_ = 'ho'
    p = 'ho*'
    print(s.isMatch(s_, p))