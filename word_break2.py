class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.s = s
        self.l = len(self.s)
        self.wordDict = wordDict
        # res_ = self.recursive(0)
        # return res_
        return self.iteration()

    def recursive(self, i):
        if i >= self.l:
            return ['']
        sub_res = []
        for j in range(i+1, self.l+1):
            if self.s[i:j] in self.wordDict:
                t = self.recursive(j)
                for t_s in t:
                    r = self.s[i:j] + ' ' + t_s if t_s != '' else self.s[i:j]
                    sub_res.append(r)
        return sub_res

    def iteration(self):
        dp = [[] for _ in range(self.l+1)]
        dp[-1].append('')
        for i in range(self.l-1, -1, -1):
            for j in range(i+1, self.l+1):
                if self.s[i:j] in self.wordDict and len(dp[j]) > 0:
                    for t_s in dp[j]:
                        r = self.s[i:j] + t_s if t_s == '' else self.s[i:j] + ' ' + t_s
                        dp[i].append(r)
        return dp[0]


if __name__ == '__main__':
    solu = Solution()
    s = 'catsanddog'
    wordDict = ['cat', 'cats', 'sand', 'and', 'dog']
    print(solu.wordBreak(s, wordDict))
