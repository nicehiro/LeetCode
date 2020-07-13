from functools import reduce


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.s = s
        self.wordDict = wordDict
        # return self.recursive(0, len(self.s))
        return self.iteration()

    def recursive(self, start, end):
        if self.s[start: end] in self.wordDict:
            return True
        for i in range(start+1, end):
            if self.s[start: i] in self.wordDict:
                res = self.recursive(i, end)
                if res:
                    return True
        return False

    def iteration(self):
        dp = [True for _ in range(len(self.s)+1)]
        for i in range(len(self.s)-1, -1, -1):
            t = [self.s[i:j] in self.wordDict and dp[j] for j in range(i+1, len(self.s)+1)]
            dp[i] = reduce(lambda x, y: x or y, t)
        return dp[0]


if __name__ == '__main__':
    solu = Solution()
    s = 'leetcode'
    wordDict = ['leet', 'code']
    print(solu.wordBreak(s, wordDict))
