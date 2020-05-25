from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) == 0:
            return ''
        self.s = s
        self.res = []
        # self.recursive(len(s), 4, [])
        # return self.res
        return self.iteration()

    def recursive(self, l, k, t: List):
        if k <= 0 and l <= 0:
            self.res.append(t)
            return
        if k <= 0 < l:
            return None
        t1 = t.copy()
        t2 = t.copy()
        t3 = t.copy()
        t1.insert(0, self.s[l-1: l])
        self.recursive(l-1, k-1, t1)
        t2.insert(0, self.s[l-2: l])
        self.recursive(l-2, k-1, t2)
        if int(self.s[l-3: l]) <= 255:
            t3.insert(0, self.s[l-3: l])
            self.recursive(l-3, k-1, t3)

    def iteration(self):
        dp = [[[] for _ in range(len(self.s))] for _ in range(4)]
        for i in range(1, len(self.s)+1):
            if self.s[0] == '0' and i >= 2:
                break
            if int(self.s[0: i]) <= 255:
                dp[0][i-1].append(self.s[0: i])
        for k in range(1, 4):
            for l in range(len(self.s)):
                for j in range(1, 4):
                    if l - j < 0:
                        break
                    elif len(self.s[l-j+1: l+1]) > 1 and self.s[l-j+1] == '0':
                        continue
                    else:
                        for temp in dp[k-1][l-j]:
                            if int(self.s[l-j+1: l+1]) <= 255:
                                # a.append(self.s[l-j+1: l+1])
                                a = temp + '.' + self.s[l-j+1: l+1]
                                dp[k][l].append(a)
        return dp[-1][-1]


if __name__ == '__main__':
    solu = Solution()
    s = ''
    print(solu.restoreIpAddresses(s))